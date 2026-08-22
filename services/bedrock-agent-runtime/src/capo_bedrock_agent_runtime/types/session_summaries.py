"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SessionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.session_summary

SessionSummaries: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.session_summary.SessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummaries) -> list:
    import capo_bedrock_agent_runtime.types.session_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.session_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SessionSummaries:
    import capo_bedrock_agent_runtime.types.session_summary

    out: SessionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.session_summary.deserialize_json(item)
        )
    return out
