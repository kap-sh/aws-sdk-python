"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_summary

AIAgentSummaryList: TypeAlias = list[
    "aws_sdk_qconnect.types.ai_agent_summary.AIAgentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentSummaryList) -> list:
    import aws_sdk_qconnect.types.ai_agent_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.ai_agent_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AIAgentSummaryList:
    import aws_sdk_qconnect.types.ai_agent_summary

    out: AIAgentSummaryList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.ai_agent_summary.deserialize_json(item))
    return out
