"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSummarizationConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class HarnessSummarizationConfiguration(TypedDict, closed=True):
    summary_ratio: NotRequired["float"]
    """<p>The ratio of content to summarize.</p>"""
    preserve_recent_messages: NotRequired["int"]
    """<p>The number of recent messages to preserve without summarization.</p>"""
    summarization_system_prompt: NotRequired["str"]
    """<p>The system prompt used for generating summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSummarizationConfiguration) -> dict:
    out: dict = {}
    if "summary_ratio" in value:
        out["summaryRatio"] = value["summary_ratio"]
    if "preserve_recent_messages" in value:
        out["preserveRecentMessages"] = value["preserve_recent_messages"]
    if "summarization_system_prompt" in value:
        out["summarizationSystemPrompt"] = value["summarization_system_prompt"]
    return out


def deserialize_json(data: dict) -> HarnessSummarizationConfiguration:
    out: HarnessSummarizationConfiguration = {}  # type: ignore[typeddict-item]
    if "summaryRatio" in data:
        out["summary_ratio"] = data["summaryRatio"]
    if "preserveRecentMessages" in data:
        out["preserve_recent_messages"] = data["preserveRecentMessages"]
    if "summarizationSystemPrompt" in data:
        out["summarization_system_prompt"] = data["summarizationSystemPrompt"]
    return out
