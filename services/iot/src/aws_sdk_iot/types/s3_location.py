"""Generated from Smithy shape ``com.amazonaws.iot#S3Location``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.s3_bucket
    import aws_sdk_iot.types.s3_key
    import aws_sdk_iot.types.s3_version


class S3Location(TypedDict):
    bucket: NotRequired["aws_sdk_iot.types.s3_bucket.S3Bucket"]
    """<p>The S3 bucket.</p>"""
    key: NotRequired["aws_sdk_iot.types.s3_key.S3Key"]
    """<p>The S3 key.</p>"""
    version: NotRequired["aws_sdk_iot.types.s3_version.S3Version"]
    """<p>The S3 bucket version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "key" in data:
        out["key"] = data["key"]
    if "version" in data:
        out["version"] = data["version"]
    return out
