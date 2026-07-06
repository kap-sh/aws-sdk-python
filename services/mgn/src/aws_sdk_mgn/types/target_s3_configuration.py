"""Generated from Smithy shape ``com.amazonaws.mgn#TargetS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.s3_bucket_name


class TargetS3Configuration(TypedDict, closed=True):
    s3_bucket: "aws_sdk_mgn.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket for target artifacts.</p>"""
    s3_bucket_owner: "aws_sdk_mgn.types.account_id.AccountID"
    """<p>The AWS account ID of the S3 bucket owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetS3Configuration) -> dict:
    out: dict = {}
    out["s3Bucket"] = value["s3_bucket"]
    out["s3BucketOwner"] = value["s3_bucket_owner"]
    return out


def deserialize_json(data: dict) -> TargetS3Configuration:
    out: TargetS3Configuration = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        raise DeserializationError("TargetS3Configuration.s3_bucket required")
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    else:
        raise DeserializationError("TargetS3Configuration.s3_bucket_owner required")
    return out
