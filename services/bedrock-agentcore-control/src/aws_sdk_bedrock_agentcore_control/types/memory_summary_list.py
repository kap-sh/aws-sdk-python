"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemorySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.memory_summary

MemorySummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.memory_summary.MemorySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemorySummaryList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.memory_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.memory_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemorySummaryList:
    import aws_sdk_bedrock_agentcore_control.types.memory_summary

    out: MemorySummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.memory_summary.deserialize_json(
                item
            )
        )
    return out
