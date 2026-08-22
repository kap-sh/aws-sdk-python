"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreMemoryRetrievalConfig``."""

from typing_extensions import NotRequired, TypedDict


class HarnessAgentCoreMemoryRetrievalConfig(TypedDict, closed=True):
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
        out["relevanceScore"] = (
            "NaN"
            if value["relevance_score"] != value["relevance_score"]
            else "Infinity"
            if value["relevance_score"] == float("inf")
            else "-Infinity"
            if value["relevance_score"] == float("-inf")
            else value["relevance_score"]
        )
    if "strategy_id" in value:
        out["strategyId"] = value["strategy_id"]
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreMemoryRetrievalConfig:
    out: HarnessAgentCoreMemoryRetrievalConfig = {}  # type: ignore[typeddict-item]
    if data.get("topK") is not None:
        out["top_k"] = data["topK"]
    if data.get("relevanceScore") is not None:
        out["relevance_score"] = float(data["relevanceScore"])
    if data.get("strategyId") is not None:
        out["strategy_id"] = data["strategyId"]
    return out
