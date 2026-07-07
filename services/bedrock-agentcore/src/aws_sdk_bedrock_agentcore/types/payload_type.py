"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PayloadType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.conversational
    import aws_sdk_bedrock_agentcore.types.memory_document


class _PayloadType_conversational(TypedDict, closed=True):
    conversational: "aws_sdk_bedrock_agentcore.types.conversational.Conversational"


class _PayloadType_blob(TypedDict, closed=True):
    blob: "aws_sdk_bedrock_agentcore.types.memory_document.MemoryDocument"


PayloadType: TypeAlias = _PayloadType_conversational | _PayloadType_blob


# --- restJson1 ser/de ---
def serialize_json(value: PayloadType) -> dict:
    if "conversational" in value:
        import aws_sdk_bedrock_agentcore.types.conversational

        return {
            "conversational": aws_sdk_bedrock_agentcore.types.conversational.serialize_json(
                value["conversational"]
            )
        }
    elif "blob" in value:
        return {"blob": value["blob"]}
    else:
        raise SerializationError("PayloadType: no variant present")


def deserialize_json(data: dict) -> PayloadType:
    if "conversational" in data:
        import aws_sdk_bedrock_agentcore.types.conversational

        return {
            "conversational": aws_sdk_bedrock_agentcore.types.conversational.deserialize_json(
                data["conversational"]
            )
        }
    elif "blob" in data:
        return {"blob": data["blob"]}
    else:
        raise DeserializationError("PayloadType: no recognized variant key")
