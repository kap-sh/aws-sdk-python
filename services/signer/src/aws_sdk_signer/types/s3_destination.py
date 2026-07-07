"""Generated from Smithy shape ``com.amazonaws.signer#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.bucket_name
    import aws_sdk_signer.types.prefix


class S3Destination(TypedDict, closed=True):
    bucket_name: NotRequired["aws_sdk_signer.types.bucket_name.BucketName"]
    """<p>Name of the S3 bucket.</p>"""
    prefix: NotRequired["aws_sdk_signer.types.prefix.Prefix"]
    """<p>An S3 prefix that you can use to limit responses to those that begin with the specified prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
