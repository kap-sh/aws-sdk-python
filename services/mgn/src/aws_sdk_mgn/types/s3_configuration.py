"""Generated from Smithy shape ``com.amazonaws.mgn#S3Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.s3_bucket_name
    import aws_sdk_mgn.types.s3_key_name


class S3Configuration(TypedDict):
    s3_bucket: NotRequired["aws_sdk_mgn.types.s3_bucket_name.S3BucketName"]
    """<p>The name of the S3 bucket.</p>"""
    s3_bucket_owner: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>The AWS account ID of the S3 bucket owner.</p>"""
    s3_key: NotRequired["aws_sdk_mgn.types.s3_key_name.S3KeyName"]
    """<p>The S3 key (path) for the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Configuration) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "s3_key" in value:
        out["s3Key"] = value["s3_key"]
    return out


def deserialize_json(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if "s3Key" in data:
        out["s3_key"] = data["s3Key"]
    return out
