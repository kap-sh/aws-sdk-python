"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserSessionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_session_summary

BrowserSessionSummaries: TypeAlias = list[
    "capo_bedrock_agentcore.types.browser_session_summary.BrowserSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSessionSummaries) -> list:
    import capo_bedrock_agentcore.types.browser_session_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.browser_session_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BrowserSessionSummaries:
    import capo_bedrock_agentcore.types.browser_session_summary

    out: BrowserSessionSummaries = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.browser_session_summary.deserialize_json(item)
        )
    return out
