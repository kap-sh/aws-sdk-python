"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.s3_location


class _ImageSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


class _ImageSource_s3Location(TypedDict, closed=True):
    s3Location: "aws_sdk_bedrock_agent_runtime.types.s3_location.S3Location"


ImageSource: TypeAlias = _ImageSource_bytes | _ImageSource_s3Location


# --- restJson1 ser/de ---
def serialize_json(value: ImageSource) -> dict:
    if "bytes" in value:
        import aws_sdk_bedrock_agent_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_agent_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    elif "s3Location" in value:
        import aws_sdk_bedrock_agent_runtime.types.s3_location

        return {
            "s3Location": aws_sdk_bedrock_agent_runtime.types.s3_location.serialize_json(
                value["s3Location"]
            )
        }
    else:
        raise SerializationError("ImageSource: no variant present")


def deserialize_json(data: dict) -> ImageSource:
    if "bytes" in data:
        import aws_sdk_bedrock_agent_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_agent_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    elif "s3Location" in data:
        import aws_sdk_bedrock_agent_runtime.types.s3_location

        return {
            "s3Location": aws_sdk_bedrock_agent_runtime.types.s3_location.deserialize_json(
                data["s3Location"]
            )
        }
    else:
        raise DeserializationError("ImageSource: no recognized variant key")
