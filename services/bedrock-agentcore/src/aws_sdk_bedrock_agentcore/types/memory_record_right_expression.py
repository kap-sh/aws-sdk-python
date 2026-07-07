"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordRightExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_metadata_value


class _MemoryRecordRightExpression_metadataValue(TypedDict, closed=True):
    metadataValue: "aws_sdk_bedrock_agentcore.types.memory_record_metadata_value.MemoryRecordMetadataValue"


MemoryRecordRightExpression: TypeAlias = _MemoryRecordRightExpression_metadataValue


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordRightExpression) -> dict:
    if "metadataValue" in value:
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_value

        return {
            "metadataValue": aws_sdk_bedrock_agentcore.types.memory_record_metadata_value.serialize_json(
                value["metadataValue"]
            )
        }
    else:
        raise SerializationError("MemoryRecordRightExpression: no variant present")


def deserialize_json(data: dict) -> MemoryRecordRightExpression:
    if "metadataValue" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_metadata_value

        return {
            "metadataValue": aws_sdk_bedrock_agentcore.types.memory_record_metadata_value.deserialize_json(
                data["metadataValue"]
            )
        }
    else:
        raise DeserializationError(
            "MemoryRecordRightExpression: no recognized variant key"
        )
