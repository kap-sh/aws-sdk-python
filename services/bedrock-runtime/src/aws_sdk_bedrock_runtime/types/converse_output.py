"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.message


class _ConverseOutput_message(TypedDict, closed=True):
    message: "aws_sdk_bedrock_runtime.types.message.Message"


ConverseOutput: TypeAlias = _ConverseOutput_message


# --- restJson1 ser/de ---
def serialize_json(value: ConverseOutput) -> dict:
    if "message" in value:
        import aws_sdk_bedrock_runtime.types.message

        return {
            "message": aws_sdk_bedrock_runtime.types.message.serialize_json(
                value["message"]
            )
        }
    else:
        raise SerializationError("ConverseOutput: no variant present")


def deserialize_json(data: dict) -> ConverseOutput:
    if "message" in data:
        import aws_sdk_bedrock_runtime.types.message

        return {
            "message": aws_sdk_bedrock_runtime.types.message.deserialize_json(
                data["message"]
            )
        }
    else:
        raise DeserializationError("ConverseOutput: no recognized variant key")
