"""Generated from Smithy shape ``com.amazonaws.iot#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.prefix
    import aws_sdk_iot.types.s3_bucket


class S3Destination(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_iot.types.s3_bucket.S3Bucket"]
    """<p>The S3 bucket that contains the updated firmware.</p>"""
    prefix: NotRequired["aws_sdk_iot.types.prefix.Prefix"]
    """<p>The S3 prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
