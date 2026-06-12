"""Generated from Smithy shape ``com.amazonaws.signer#S3SignedObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.bucket_name
    import aws_sdk_signer.types.key


class S3SignedObject(TypedDict):
    bucket_name: NotRequired["aws_sdk_signer.types.bucket_name.BucketName"]
    """<p>Name of the S3 bucket.</p>"""
    key: NotRequired["aws_sdk_signer.types.key.Key"]
    """<p>Key name that uniquely identifies a signed code image in your bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3SignedObject) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "key" in value:
        out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3SignedObject:
    out: S3SignedObject = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "key" in data:
        out["key"] = data["key"]
    return out
