"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_metadata_value
    import aws_sdk_bedrock_agentcore.types.metadata_key

MemoryRecordMetadataMap: TypeAlias = dict[
    "aws_sdk_bedrock_agentcore.types.metadata_key.MetadataKey",
    "aws_sdk_bedrock_agentcore.types.memory_record_metadata_value.MemoryRecordMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MemoryRecordMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_value

        out[key] = (
            aws_sdk_bedrock_agentcore.types.memory_record_metadata_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryRecordMetadataMap:
    out: MemoryRecordMetadataMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_value

        out[key] = (
            aws_sdk_bedrock_agentcore.types.memory_record_metadata_value.deserialize_json(
                value
            )
        )
    return out
