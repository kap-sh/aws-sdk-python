"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseImageSource``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError


class _GuardrailConverseImageSource_bytes(TypedDict):
    bytes: "bytes"


GuardrailConverseImageSource: TypeAlias = _GuardrailConverseImageSource_bytes


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseImageSource) -> dict:
    if "bytes" in value:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    else:
        raise SerializationError("GuardrailConverseImageSource: no variant present")


def deserialize_json(data: dict) -> GuardrailConverseImageSource:
    if "bytes" in data:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    else:
        raise DeserializationError(
            "GuardrailConverseImageSource: no recognized variant key"
        )
