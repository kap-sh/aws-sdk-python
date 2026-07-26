"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AudioSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.s3_location


class _AudioSource_bytes(TypedDict, closed=True):
    bytes: "bytes"


class _AudioSource_s3Location(TypedDict, closed=True):
    s3Location: "capo_bedrock_runtime.types.s3_location.S3Location"


AudioSource: TypeAlias = _AudioSource_bytes | _AudioSource_s3Location


# --- restJson1 ser/de ---
def serialize_json(value: AudioSource) -> dict:
    if "bytes" in value:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.serialize_json(
                value["bytes"]
            )
        }
    elif "s3Location" in value:
        import capo_bedrock_runtime.types.s3_location

        return {
            "s3Location": capo_bedrock_runtime.types.s3_location.serialize_json(
                value["s3Location"]
            )
        }
    else:
        raise SerializationError("AudioSource: no variant present")


def deserialize_json(data: dict) -> AudioSource:
    if "bytes" in data:
        import capo_bedrock_runtime.types._prelude.blob

        return {
            "bytes": capo_bedrock_runtime.types._prelude.blob.deserialize_json(
                data["bytes"]
            )
        }
    elif "s3Location" in data:
        import capo_bedrock_runtime.types.s3_location

        return {
            "s3Location": capo_bedrock_runtime.types.s3_location.deserialize_json(
                data["s3Location"]
            )
        }
    else:
        raise DeserializationError("AudioSource: no recognized variant key")
