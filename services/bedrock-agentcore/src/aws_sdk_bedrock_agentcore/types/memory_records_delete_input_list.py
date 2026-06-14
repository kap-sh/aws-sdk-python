"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordsDeleteInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_delete_input

MemoryRecordsDeleteInputList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.memory_record_delete_input.MemoryRecordDeleteInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordsDeleteInputList) -> list:
    import aws_sdk_bedrock_agentcore.types.memory_record_delete_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_record_delete_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemoryRecordsDeleteInputList:
    import aws_sdk_bedrock_agentcore.types.memory_record_delete_input

    out: MemoryRecordsDeleteInputList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_record_delete_input.deserialize_json(
                item
            )
        )
    return out
