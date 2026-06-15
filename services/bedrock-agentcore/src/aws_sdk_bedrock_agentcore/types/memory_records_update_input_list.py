"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordsUpdateInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_update_input

MemoryRecordsUpdateInputList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.memory_record_update_input.MemoryRecordUpdateInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordsUpdateInputList) -> list:
    import aws_sdk_bedrock_agentcore.types.memory_record_update_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_record_update_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemoryRecordsUpdateInputList:
    import aws_sdk_bedrock_agentcore.types.memory_record_update_input

    out: MemoryRecordsUpdateInputList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_record_update_input.deserialize_json(
                item
            )
        )
    return out
