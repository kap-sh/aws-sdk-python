"""Generated from Smithy shape ``com.amazonaws.qconnect#AIAgentVersionSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_version_summary

AIAgentVersionSummariesList: TypeAlias = list[
    "aws_sdk_qconnect.types.ai_agent_version_summary.AIAgentVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AIAgentVersionSummariesList) -> list:
    import aws_sdk_qconnect.types.ai_agent_version_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.ai_agent_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AIAgentVersionSummariesList:
    import aws_sdk_qconnect.types.ai_agent_version_summary

    out: AIAgentVersionSummariesList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.ai_agent_version_summary.deserialize_json(item)
        )
    return out
