"""Minimal OTel bootstrap for the mcpgw service (Issue #1122).

This module starts a Prometheus exposition listener on
``OTEL_EXPORTER_PROMETHEUS_HOST:OTEL_EXPORTER_PROMETHEUS_PORT`` so the
in-cluster Prometheus can scrape mcpgw alongside registry and auth-server.

Today mcpgw declares no application-defined OTel meters (issue #1123
tracks that follow-up). The endpoint will still serve the default
``python_*`` and ``process_*`` runtime metrics that ``prometheus_client``
exposes automatically, plus any future application meters added later
without further bootstrap changes.

Mirrors the helper in ``registry/observability/meters.py`` and
``auth_server/observability/meters.py``. We do not import from the
registry meter module here because mcpgw is a separate Docker image
that does NOT include the registry codebase.
"""

from __future__ import annotations

import logging
import os

logger = logging.getLogger(__name__)


def init_meter_provider_if_needed() -> None:
    """Bootstrap the OTel SDK + Prometheus exporter when applicable.

    No-op when:
    - ``OTEL_EXPORTER_PROMETHEUS_HOST`` is unset (operator hasn't opted in).
    - A real ``MeterProvider`` is already installed (e.g., by
      ``opentelemetry-instrument`` doing its job).
    """
    prom_host = os.getenv("OTEL_EXPORTER_PROMETHEUS_HOST", "").strip()
    if not prom_host:
        return

    try:
        from opentelemetry import metrics
    except ImportError:
        logger.debug("opentelemetry SDK not installed; skipping bootstrap")
        return

    current = metrics.get_meter_provider()
    current_name = type(current).__name__
    if "ProxyMeterProvider" not in current_name and "NoOp" not in current_name:
        return

    try:
        from opentelemetry.exporter.prometheus import PrometheusMetricReader
        from opentelemetry.sdk.metrics import MeterProvider
        from prometheus_client import start_http_server
    except ImportError as exc:
        logger.warning(
            "Cannot start Prometheus exporter: %s. Install "
            "opentelemetry-exporter-prometheus and prometheus-client.",
            exc,
        )
        return

    prom_port = int(os.getenv("OTEL_EXPORTER_PROMETHEUS_PORT", "9464"))
    try:
        start_http_server(port=prom_port, addr=prom_host)
        reader = PrometheusMetricReader()
        provider = MeterProvider(metric_readers=[reader])
        metrics.set_meter_provider(provider)
        logger.info(
            "Started OTel Prometheus exporter on %s:%d (provider=MeterProvider)",
            prom_host,
            prom_port,
        )
    except OSError as exc:
        logger.warning(
            "Could not start Prometheus exporter on %s:%d: %s",
            prom_host,
            prom_port,
            exc,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("OTel Prometheus exporter init failed: %s", exc)
