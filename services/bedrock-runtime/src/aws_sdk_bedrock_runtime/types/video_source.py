"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#VideoSource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.s3_location


class _VideoSource_bytes(TypedDict):
    bytes: "bytes"


class _VideoSource_s3Location(TypedDict):
    s3Location: "aws_sdk_bedrock_runtime.types.s3_location.S3Location"


VideoSource: TypeAlias = _VideoSource_bytes | _VideoSource_s3Location


# --- restJson1 ser/de ---
def serialize_json(value: VideoSource) -> dict:
    if "bytes" in value:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    elif "s3Location" in value:
        import aws_sdk_bedrock_runtime.types.s3_location

        return {
            "s3Location": aws_sdk_bedrock_runtime.types.s3_location.serialize_json(
                value["s3Location"]
            )
        }
    else:
        raise SerializationError("VideoSource: no variant present")


def deserialize_json(data: dict) -> VideoSource:
    if "bytes" in data:
        import aws_sdk_bedrock_runtime.types._prelude.blob

        return {
            "bytes": aws_sdk_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    elif "s3Location" in data:
        import aws_sdk_bedrock_runtime.types.s3_location

        return {
            "s3Location": aws_sdk_bedrock_runtime.types.s3_location.deserialize_json(
                data["s3Location"]
            )
        }
    else:
        raise DeserializationError("VideoSource: no recognized variant key")
