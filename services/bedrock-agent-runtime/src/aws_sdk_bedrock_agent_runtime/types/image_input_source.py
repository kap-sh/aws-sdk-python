"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInputSource``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)


class _ImageInputSource_bytes(TypedDict):
    bytes: "bytes"


ImageInputSource: TypeAlias = _ImageInputSource_bytes


# --- restJson1 ser/de ---
def serialize_json(value: ImageInputSource) -> dict:
    if "bytes" in value:
        import aws_sdk_bedrock_agent_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_agent_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    else:
        raise SerializationError("ImageInputSource: no variant present")


def deserialize_json(data: dict) -> ImageInputSource:
    if "bytes" in data:
        import aws_sdk_bedrock_agent_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_agent_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    else:
        raise DeserializationError("ImageInputSource: no recognized variant key")
