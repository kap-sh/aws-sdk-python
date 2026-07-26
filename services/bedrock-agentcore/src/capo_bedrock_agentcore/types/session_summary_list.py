"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_summary

SessionSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.session_summary.SessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummaryList) -> list:
    import capo_bedrock_agentcore.types.session_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.session_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionSummaryList:
    import capo_bedrock_agentcore.types.session_summary

    out: SessionSummaryList = []
    for item in data:
        out.append(capo_bedrock_agentcore.types.session_summary.deserialize_json(item))
    return out
