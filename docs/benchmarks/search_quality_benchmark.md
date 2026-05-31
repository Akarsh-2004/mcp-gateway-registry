# Search Benchmark Report

- **Target:** http://localhost
- **Timestamp:** 2026-05-31T16:30:18
- **Version:** 1.24.3-7-gf0fb7768-fix/hybrid-search-rrf-scoring
- **Database:** mongodb-ce
- **Registry contents:** 134 servers, 119 agents, 109 skills
- **Queries:** 100 total, 99 succeeded, 1 failed
- **Avg latency:** 105ms per query

## Quality Metrics (against ground truth)

| Metric | Value |
|--------|-------|
| NDCG@10 (avg) | 0.6857 |
| MRR (avg) | 0.7173 |
| Recall@10 (avg) | 0.7549 |
| Perfect queries (NDCG=1.0) | 42 / 95 |
| Zero-hit queries (NDCG=0.0) | 14 / 95 |
| Evaluated queries | 95 (queries with ground truth expectations) |
| Skipped from eval | 4 (no-answer queries with empty expected results) |
| Failed queries | 1 (API rejected, e.g. empty query) |

## Score Health

| Metric | Value |
|--------|-------|
| Total scores in results | 979 |
| Unique score values | 435 |
| Saturated at 1.0 | 115 (11%) |
| Score range | 0.2475 to 1.0000 |

## Quality by Category

| Category | Queries | NDCG@10 | MRR | Recall@10 |
|----------|---------|---------|-----|----------|
| agent-focused | 10 | 0.431 | 0.514 | 0.647 |
| conflict-ambiguous | 4 | 0.729 | 0.875 | 0.750 |
| conflict-vector-vs-lexical | 6 | 0.645 | 0.833 | 0.556 |
| exact-name | 10 | 0.900 | 0.900 | 0.900 |
| multi-entity | 10 | 0.783 | 0.917 | 0.758 |
| no-answer | 6 | 0.564 | 0.533 | 0.667 |
| semantic | 10 | 0.661 | 0.612 | 0.850 |
| skill-focused | 10 | 0.186 | 0.143 | 0.400 |
| tool-precision | 10 | 1.000 | 1.000 | 1.000 |
| tricky | 19 | 0.808 | 0.820 | 0.833 |

## Results by Query

### "cloudflare"

*Exact product name in server names and tags*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai-registry/cloudflare-docs, /cloudflare-api, /cloudflare-docs

Latency: 97ms | Results: 7 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | Cloudflare Documentation MCP Server | 1.0000 |
| 2 | cloudlfare-api | 0.9866 |
| 3 | Cloudflare Documentation MCP Server | 0.9741 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | search_cloudflare_documentation | 0.6500 |
| 2 | search | 0.5100 |
| 3 | execute | 0.5100 |
| 4 | search_cloudflare_documentation | 0.6500 |

---

### "context7"

*Exact server name (single word)*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /context7, /ai-registry/context7

Latency: 103ms | Results: 6 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | context7 | 1.0000 |
| 2 | Context7 MCP Server | 0.9714 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | resolve-library-id | 0.5100 |
| 2 | query-docs | 0.5100 |
| 3 | resolve-library-id | 0.5100 |
| 4 | query-docs | 0.5100 |

---

### "Exa"

*Short exact product name (3 chars, tests min token length)*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai.exa-exa

Latency: 112ms | Results: 10 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.exa/exa | 1.0000 |
| 2 | ai.gethal/mcp | 0.6329 |
| 3 | Complete Server Example | 0.4829 |
| 4 | ai.autonomad/travel | 0.4436 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | web_search_exa | 0.6500 |
| 2 | web_fetch_exa | 0.6500 |
| 3 | get_use_cases | 0.5100 |
| 4 | create_booking_intent | 0.5100 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.4464 |

**Skills:**

| # | Name | Score |
|---|------|-------|
| 1 | documentation-lookup | 0.3963 |

---

### "NotebookLM"

*CamelCase product name*

NDCG@10=0.000 | MRR=0.000 | Recall=0.00 | Missing: /skills/notebooklm

Latency: 97ms | Results: 7 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.autonomad/travel | 0.7531 |
| 2 | ai.gossiper/shopify-admin-mcp | 0.6354 |
| 3 | agency.lona/trading | 0.5214 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.4108 |
| 2 | None | 0.3035 |

**Skills:**

| # | Name | Score |
|---|------|-------|
| 1 | claude-api | 1.0000 |
| 2 | new-feature-design | 0.8746 |

---

### "SpotDB"

*Mixed case product name*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /spotdb

Latency: 153ms | Results: 1 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | SpotDB | 1.0000 |

---

### "hydrata"

*Organization/product name in path*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /com.hydrata-hydrata-mcp-server

Latency: 201ms | Results: 1 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | com.hydrata/hydrata-mcp-server | 1.0000 |

---

### "strava"

*Fitness app name in path*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai.com.mcp-strava

Latency: 229ms | Results: 1 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.com.mcp/strava | 1.0000 |

---

### "linkedin"

*Social network name*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai.com.mcp-linkedin

Latency: 113ms | Results: 4 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.com.mcp/linkedin | 1.0000 |
| 2 | ai.exa/exa | 0.9571 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | createSharePost | 0.5100 |
| 2 | web_search_exa | 0.5100 |

---

### "petstore"

*Classic API example name*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai.com.mcp-petstore

Latency: 108ms | Results: 1 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.com.mcp/petstore | 1.0000 |

---

### "QuizCrafter"

*Agent name with compound word*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /quizcrafter-agent

Latency: 105ms | Results: 1 total

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 1.0000 |

---

### "I need to find information about a place to stay during vacation"

*Natural language for hotel/travel search (no keywords match directly)*

NDCG@10=0.787 | MRR=1.000 | Recall=0.50 | Found: /ai.autonomad-travel | Missing: /travel-assistant-agent

Latency: 105ms | Results: 13 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.autonomad/travel | 1.0000 |
| 2 | AI Registry tools | 0.7041 |
| 3 | test-placeholder | 0.7003 |
| 4 | aws-kb | 0.6716 |
| 5 | AI Registry tools | 0.6656 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | search_hotels | 0.7586 |
| 2 | search_flights | 0.2529 |
| 3 | search_dining | 0.5057 |
| 4 | search_activities | 0.2529 |
| 5 | search_events | 0.2529 |

**Skills:**

| # | Name | Score |
|---|------|-------|
| 1 | documentation-lookup | 0.3749 |

---

### "something to help me when my app is down and I need to fix it fast"

*Incident response paraphrase (no keyword overlap with SRE tools)*

NDCG@10=0.000 | MRR=0.000 | Recall=0.00 | Missing: /sre-gateway

Latency: 114ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.dreamlit/mcp | 1.0000 |
| 2 | ai.demanddiscovery/mcp | 0.8579 |
| 3 | com.hydrata/hydrata-mcp-server | 0.6524 |
| 4 | ai.exa/exa | 0.5698 |
| 5 | aws-kb | 0.3982 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | get_status | 0.7425 |
| 2 | create_or_update_workflow | 0.7425 |
| 3 | list_projects | 0.4950 |
| 4 | list_workflows | 0.2475 |
| 5 | list_brand_kits | 0.6350 |

---

### "what tools can analyze if my servers are overloaded"

*Resource monitoring expressed conversationally*

NDCG@10=0.356 | MRR=0.167 | Recall=1.00 | Found: /sre-gateway

Latency: 105ms | Results: 14 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | Real Server Fake Tools | 1.0000 |
| 2 | AI Registry tools | 0.9431 |
| 3 | ai.arclan/registry | 0.9140 |
| 4 | AI Registry tools | 0.9140 |
| 5 | ai.com.mcp/registry | 0.8960 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | quantum_flux_analyzer | 0.4250 |
| 2 | user_profile_analyzer | 0.4250 |
| 3 | list_services | 0.5700 |
| 4 | search_registry | 0.5700 |
| 5 | intelligent_tool_finder | 0.2850 |

**Skills:**

| # | Name | Score |
|---|------|-------|
| 1 | mcp-builder | 0.6649 |
| 2 | pr-review | 0.5657 |

---

### "create an image from text description"

*Image generation (maps to OpenAI createImage tool)*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai.com.mcp-openai-tools

Latency: 96ms | Results: 14 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.com.mcp/openai-tools | 1.0000 |
| 2 | ai.filegraph/document-processing | 0.9438 |
| 3 | ai.dreamlit/mcp | 0.6900 |
| 4 | ai.auteng/docs | 0.6879 |
| 5 | ai.com.mcp/lenny-rachitsky-podcast | 0.6256 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | createImage | 0.8500 |
| 2 | createImageEdit | 0.8500 |
| 3 | createImageVariation | 0.8500 |
| 4 | createTranscription | 0.4250 |
| 5 | createTranslation | 0.4250 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.5732 |
| 2 | None | 0.3302 |

---

### "figure out what time it is in Tokyo"

*Timezone query in natural language*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai-registry/currenttime/, /currenttime/

Latency: 106ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | Current Time API | 1.0000 |
| 2 | Current Time API | 0.9505 |
| 3 | Weather Time Observability Gateway | 0.8568 |
| 4 | ai.autonomad/travel | 0.7733 |
| 5 | ai.com.mcp/strava | 0.3316 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | current_time_by_timezone | 0.4250 |
| 2 | current_time_by_timezone | 0.4250 |
| 3 | agentcore-time-tool-target___get_time | 0.4250 |
| 4 | search_hotels | 0.2850 |
| 5 | search_flights | 0.2850 |

---

### "help parents understand their child's mental health"

*Child psychology resources (no keywords match tool names)*

NDCG@10=0.959 | MRR=1.000 | Recall=1.00 | Found: /ai.childpsychiatry-library, /ai.childadhd-library, /ai.childanxiety-library

Latency: 108ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.childpsychiatry/library | 1.0000 |
| 2 | ai.childadhd/library | 1.0000 |
| 3 | ai.childanxiety/library | 0.9996 |
| 4 | MCP Gateway Tools | 0.8193 |
| 5 | ac.tandem/docs-mcp | 0.7293 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | search_articles | 0.2529 |
| 2 | list_articles | 0.2529 |
| 3 | get_article | 0.2529 |
| 4 | cite_article | 0.2529 |
| 5 | get_microsite_info | 0.5057 |

---

### "how do I make my email marketing campaigns better"

*Marketing workflow (maps to Dreamlit which does workflows/campaigns)*

NDCG@10=0.387 | MRR=0.200 | Recall=1.00 | Found: /ai.dreamlit-mcp

Latency: 107ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.demanddiscovery/mcp | 1.0000 |
| 2 | ai.adadvisor/mcp-server | 0.9588 |
| 3 | ai.gethal/mcp | 0.9188 |
| 4 | aws-kb | 0.6486 |
| 5 | ai.dreamlit/mcp | 0.6268 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | ask_demand_discovery | 0.2700 |
| 2 | compare_validation_approaches | 0.5400 |
| 3 | start_demand_report | 0.2700 |
| 4 | get_company_info | 0.2700 |
| 5 | book_demo | 0.2700 |

---

### "verify if a payment system is working correctly"

*Payment verification (AgenticTerminal has verify_payment_endpoint)*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai.agenticterminal-directory

Latency: 96ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.agenticterminal/directory | 1.0000 |
| 2 | ai.agenticshelf/mcp | 0.8661 |
| 3 | ai.agenticshelf/graffeo | 0.8535 |
| 4 | ai.com.mcp/petstore | 0.6730 |
| 5 | ai.autonomad/travel | 0.6369 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | get_merchant | 0.2700 |
| 2 | verify_payment_endpoint | 0.8200 |
| 3 | list_rails | 0.2700 |
| 4 | list_products | 0.2700 |
| 5 | list_products | 0.2700 |

---

### "teach employees about our product through interactive exercises"

*Training/quiz creation paraphrase*

NDCG@10=0.431 | MRR=0.250 | Recall=1.00 | Found: /quizcrafter-agent

Latency: 107ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.demanddiscovery/mcp | 1.0000 |
| 2 | ai.agenticshelf/mcp | 0.4747 |
| 3 | ai.agenticshelf/graffeo | 0.4584 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | ask_demand_discovery | 0.2600 |
| 2 | get_product_details | 0.4000 |
| 3 | explain_demand_signals | 0.5200 |
| 4 | get_data_source_categories | 0.4000 |
| 5 | start_demand_report | 0.5200 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.7573 |
| 2 | None | 0.6381 |

**Skills:**

| # | Name | Score |
|---|------|-------|
| 1 | xlsx | 0.3059 |

---

### "check how much something costs in our store"

*Price lookup paraphrase (AgenticShelf has get_price)*

NDCG@10=0.693 | MRR=0.500 | Recall=1.00 | Found: /ai.agenticshelf-mcp, /ai.agenticshelf-graffeo

Latency: 120ms | Results: 14 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.demanddiscovery/mcp | 1.0000 |
| 2 | ai.agenticshelf/mcp | 0.9621 |
| 3 | ai.agenticshelf/graffeo | 0.9504 |
| 4 | ai.com.mcp/petstore | 0.9504 |
| 5 | SRE Gateway | 0.6119 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | get_product_details | 0.2600 |
| 2 | explain_demand_signals | 0.2600 |
| 3 | get_data_source_categories | 0.4000 |
| 4 | start_demand_report | 0.2600 |
| 5 | check_stock | 0.4000 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.6364 |
| 2 | None | 0.5727 |

---

### "search"

*Extremely common word - appears in 20+ tools. Vector picks semantic intent, lexical matches everything.*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /ai-registry/airegistry-tools/, /ai.exa-exa, /airegistry-tools/

Latency: 87ms | Results: 14 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | AI Registry tools | 1.0000 |
| 2 | ai.exa/exa | 0.9708 |
| 3 | AI Registry tools | 0.9708 |
| 4 | record_novacolor_italian_finishes | 0.9295 |
| 5 | ai.autonomad/travel | 0.9295 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | list_services | 0.5100 |
| 2 | list_agents | 0.5100 |
| 3 | list_skills | 0.5100 |
| 4 | get_skill_content | 0.5100 |
| 5 | search_registry | 0.6500 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.7702 |
| 2 | None | 0.7477 |

---

### "list"

*Generic verb - many tools have 'list' prefix. Tests disambiguation.*

NDCG@10=0.613 | MRR=1.000 | Recall=0.50 | Found: /ai-registry/airegistry-tools/ | Missing: /ai-registry/mcpgw/

Latency: 92ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | AI Registry tools | 1.0000 |
| 2 | AI Registry tools | 0.9498 |
| 3 | ai.com.mcp/strava | 0.5928 |
| 4 | context7 | 0.5613 |
| 5 | io.github.OneNicolas/mcp-service-public | 0.4463 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | list_services | 0.6500 |
| 2 | list_agents | 0.6500 |
| 3 | list_skills | 0.6500 |
| 4 | get_skill_content | 0.5100 |
| 5 | list_services | 0.6500 |

---

### "documentation"

*Broad term - matches many docs semantically and lexically*

NDCG@10=0.780 | MRR=1.000 | Recall=1.00 | Found: /agentcore-aws-kb, /ai-registry/cloudflare-docs, /cloudflare-docs

Latency: 87ms | Results: 14 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | aws-kb | 0.8509 |
| 2 | Cloudflare Documentation MCP Server | 0.7799 |
| 3 | Cloudflare Documentation MCP Server | 0.7619 |
| 4 | context7 | 0.5850 |
| 5 | Complete Server Example | 0.5793 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | aws___read_documentation | 0.6500 |
| 2 | aws___search_documentation | 0.6500 |
| 3 | aws___recommend | 0.5100 |
| 4 | aws___list_regions | 0.5100 |
| 5 | aws___get_regional_availability | 0.5100 |

**Skills:**

| # | Name | Score |
|---|------|-------|
| 1 | documentation-lookup | 1.0000 |
| 2 | new-feature-design | 0.7864 |

---

### "agent"

*Core platform concept - appears everywhere. What should rank first?*

NDCG@10=0.521 | MRR=0.500 | Recall=0.50 | Found: /agenttrust-mcp | Missing: /weather-time-observability-agent

Latency: 90ms | Results: 7 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.agenticterminal/directory | 1.0000 |
| 2 | AgentTrust MCP | 0.4863 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | search_merchants | 0.5100 |
| 2 | whoami | 0.5100 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.6653 |
| 2 | None | 0.4097 |
| 3 | None | 0.2998 |

---

### "fetch data from a website"

*Vector: web crawling. Lexical: 'fetch' tool exists in novacolor server.*

NDCG@10=0.587 | MRR=1.000 | Recall=0.33 | Found: /ai.exa-exa | Missing: /skills/anysite-cli, /agentcore-record-novacolor-italian-finishes

Latency: 99ms | Results: 13 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.exa/exa | 1.0000 |
| 2 | ai.baselight/baselight | 1.0000 |
| 3 | agency.lona/trading | 0.9980 |
| 4 | ai.com.mcp/linkedin | 0.9502 |
| 5 | ai.adadvisor/mcp-server | 0.8582 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | web_search_exa | 0.3100 |
| 2 | web_fetch_exa | 0.7600 |
| 3 | baselight_search_catalog | 0.3100 |
| 4 | baselight_search_tables | 0.3100 |
| 5 | baselight_get_dataset_metadata | 0.4500 |

**Skills:**

| # | Name | Score |
|---|------|-------|
| 1 | xlsx | 0.5424 |

---

### "recommend"

*Lexical: aws___recommend tool. Vector: recommendation system concept.*

NDCG@10=0.765 | MRR=1.000 | Recall=0.67 | Found: /ai.arclan-registry, /agentcore-aws-kb | Missing: /aws-kb

Latency: 81ms | Results: 6 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.arclan/registry | 1.0000 |
| 2 | aws-kb | 0.7343 |
| 3 | ai.dreamlit/mcp | 0.6398 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | recommend_server | 0.6500 |
| 2 | aws___recommend | 0.6500 |
| 3 | get_status | 0.5100 |

---

### "products"

*Lexical: appears in multiple servers (novacolor, agenticshelf). Vector: e-commerce concept.*

NDCG@10=0.845 | MRR=1.000 | Recall=1.00 | Found: /agentcore-record-novacolor-italian-finishes, /ai.agenticshelf-graffeo, /ai.agenticshelf-mcp

Latency: 90ms | Results: 13 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | record_novacolor_italian_finishes | 1.0000 |
| 2 | ai.agenticshelf/graffeo | 0.5707 |
| 3 | ai.agenticshelf/mcp | 0.4516 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | search_site_products | 0.6500 |
| 2 | search | 0.5100 |
| 3 | list_products | 0.6500 |
| 4 | search_products | 0.6500 |
| 5 | list_products | 0.6500 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 0.6089 |
| 2 | None | 0.5852 |
| 3 | None | 0.4308 |
| 4 | None | 0.3997 |

---

### "run simulation and check status"

*Lexical: 'simulation' + 'status'. Vector: scientific computing workflow.*

NDCG@10=1.000 | MRR=1.000 | Recall=1.00 | Found: /com.hydrata-hydrata-mcp-server

Latency: 88ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | com.hydrata/hydrata-mcp-server | 1.0000 |
| 2 | ai.dreamlit/mcp | 0.8862 |
| 3 | ai.demanddiscovery/mcp | 0.7616 |
| 4 | SRE Gateway | 0.7190 |
| 5 | ai.agenticshelf/mcp | 0.7043 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | list_projects | 0.5400 |
| 2 | get_project | 0.2700 |
| 3 | get_scenario | 0.8100 |
| 4 | start_simulation | 0.8800 |
| 5 | get_run_status | 1.0000 |

---

### "calculate"

*Lexical: calculator tool exists. Vector: math/computation concept.*

NDCG@10=0.000 | MRR=0.000 | Recall=0.00 | Missing: /io-example-calculator-mcp, /weather-time-observability-gateway

Latency: 90ms | Results: 7 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | ai.com.mcp/strava | 0.9224 |
| 2 | io.github.OneNicolas/mcp-service-public | 0.7744 |
| 3 | ai.gethal/mcp | 0.7038 |
| 4 | com.hydrata/hydrata-mcp-server | 0.6354 |
| 5 | ai.autonomad/travel | 0.5690 |

**Agents:**

| # | Name | Score |
|---|------|-------|
| 1 | None | 1.0000 |

---

### "health check monitoring"

*Lexical: healthcheck tool in registry. Vector: observability concept.*

NDCG@10=0.674 | MRR=1.000 | Recall=0.33 | Found: /sre-gateway | Missing: /ai-registry/airegistry-tools/, /airegistry-tools/

Latency: 91ms | Results: 12 total

**Servers:**

| # | Name | Score |
|---|------|-------|
| 1 | SRE Gateway | 1.0000 |
| 2 | MCP Gateway Tools | 0.9677 |
| 3 | ai.agenticshelf/mcp | 0.9215 |
| 4 | ai.agenticshelf/graffeo | 0.9100 |
| 5 | ai.arclan/registry | 0.8998 |

**Tools:**

| # | Name | Score |
|---|------|-------|
| 1 | k8s-api___get_deployment_status | 0.6200 |
| 2 | k8s-api___get_node_status | 0.6200 |
| 3 | metrics-api___get_availability_metrics | 0.3100 |
| 4 | healthcheck | 0.9000 |
| 5 | check_stock | 0.4500 |

---

## Failed Queries

| Query | Error |
|-------|-------|
|  | 400 Client Error: Bad Request for url: http://localhost/api/search/semantic |
