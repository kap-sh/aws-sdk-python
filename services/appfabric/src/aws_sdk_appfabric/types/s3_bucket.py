"""Generated from Smithy shape ``com.amazonaws.appfabric#S3Bucket``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.string63
    import aws_sdk_appfabric.types.string120


class S3Bucket(TypedDict):
    bucket_name: "aws_sdk_appfabric.types.string63.String63"
    """<p>The name of the Amazon S3 bucket.</p>"""
    prefix: NotRequired["aws_sdk_appfabric.types.string120.String120"]
    """<p>The object key to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Bucket) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3Bucket:
    out: S3Bucket = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3Bucket.bucket_name required")
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
