"""Generated from Smithy shape ``com.amazonaws.mgn#S3BucketSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.s3_bucket_name
    import aws_sdk_mgn.types.s3_key


class S3BucketSource(TypedDict):
    s3_bucket: "aws_sdk_mgn.types.s3_bucket_name.S3BucketName"
    """<p>S3 bucket source s3 bucket.</p>"""
    s3_key: "aws_sdk_mgn.types.s3_key.S3Key"
    """<p>S3 bucket source s3 key.</p>"""
    s3_bucket_owner: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>S3 bucket source s3 bucket owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketSource) -> dict:
    out: dict = {}
    out["s3Bucket"] = value["s3_bucket"]
    out["s3Key"] = value["s3_key"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3BucketSource:
    out: S3BucketSource = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        raise DeserializationError("S3BucketSource.s3_bucket required")
    if "s3Key" in data:
        out["s3_key"] = data["s3Key"]
    else:
        raise DeserializationError("S3BucketSource.s3_key required")
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    return out
