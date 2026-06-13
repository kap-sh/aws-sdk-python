"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreMemoryRetrievalConfig``."""

from typing import TypedDict
from typing_extensions import NotRequired

class HarnessAgentCoreMemoryRetrievalConfig(TypedDict):
    top_k: NotRequired["int"]
    """<p>The maximum number of memory entries to retrieve.</p>"""
    relevance_score: NotRequired["float"]
    """<p>The minimum relevance score for retrieved memories.</p>"""
    strategy_id: NotRequired["str"]
    """<p>The ID of the retrieval strategy to use.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreMemoryRetrievalConfig) -> dict:
    out: dict = {}
    if "top_k" in value:
        out["topK"] = value["top_k"]
    if "relevance_score" in value:
        out["relevanceScore"] = value["relevance_score"]
    if "strategy_id" in value:
        out["strategyId"] = value["strategy_id"]
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreMemoryRetrievalConfig:
    out: HarnessAgentCoreMemoryRetrievalConfig = {}  # type: ignore[typeddict-item]
    if "topK" in data:
        out["top_k"] = data["topK"]
    if "relevanceScore" in data:
        out["relevance_score"] = data["relevanceScore"]
    if "strategyId" in data:
        out["strategy_id"] = data["strategyId"]
    return out