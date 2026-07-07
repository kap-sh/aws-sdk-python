"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobS3OutputConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.key_prefix


class ProtectedJobS3OutputConfigurationOutput(TypedDict, closed=True):
    bucket: "str"
    """<p> The S3 bucket for job output.</p>"""
    key_prefix: NotRequired["aws_sdk_cleanrooms.types.key_prefix.KeyPrefix"]
    """<p>The S3 prefix to unload the protected job results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobS3OutputConfigurationOutput) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_json(data: dict) -> ProtectedJobS3OutputConfigurationOutput:
    out: ProtectedJobS3OutputConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError(
            "ProtectedJobS3OutputConfigurationOutput.bucket required"
        )
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    return out
