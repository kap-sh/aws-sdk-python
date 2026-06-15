"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_summary

MemoryRecordSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.memory_record_summary.MemoryRecordSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordSummaryList) -> list:
    import aws_sdk_bedrock_agentcore.types.memory_record_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_record_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemoryRecordSummaryList:
    import aws_sdk_bedrock_agentcore.types.memory_record_summary

    out: MemoryRecordSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_record_summary.deserialize_json(item)
        )
    return out
