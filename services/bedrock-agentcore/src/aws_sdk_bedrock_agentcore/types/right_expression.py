"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RightExpression``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.metadata_value


class _RightExpression_metadataValue(TypedDict):
    metadataValue: "aws_sdk_bedrock_agentcore.types.metadata_value.MetadataValue"


RightExpression: TypeAlias = _RightExpression_metadataValue


# --- restJson1 ser/de ---
def serialize_json(value: RightExpression) -> dict:
    if "metadataValue" in value:
        import aws_sdk_bedrock_agentcore.types.metadata_value

        return {
            "metadataValue": aws_sdk_bedrock_agentcore.types.metadata_value.serialize_json(
                value["metadataValue"]
            )
        }
    else:
        raise SerializationError("RightExpression: no variant present")


def deserialize_json(data: dict) -> RightExpression:
    if "metadataValue" in data:
        import aws_sdk_bedrock_agentcore.types.metadata_value

        return {
            "metadataValue": aws_sdk_bedrock_agentcore.types.metadata_value.deserialize_json(
                data["metadataValue"]
            )
        }
    else:
        raise DeserializationError("RightExpression: no recognized variant key")
