"""Generated from Smithy shape ``com.amazonaws.dynamodb#S3BucketSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.s3_bucket
    import aws_sdk_dynamodb.types.s3_bucket_owner
    import aws_sdk_dynamodb.types.s3_prefix


class S3BucketSource(TypedDict):
    s3_bucket_owner: NotRequired["aws_sdk_dynamodb.types.s3_bucket_owner.S3BucketOwner"]
    """<p> The account number of the S3 bucket that is being imported from. If the bucket is owned by the requester this is optional. </p>"""
    s3_bucket: "aws_sdk_dynamodb.types.s3_bucket.S3Bucket"
    """<p> The S3 bucket that is being imported from. </p>"""
    s3_key_prefix: NotRequired["aws_sdk_dynamodb.types.s3_prefix.S3Prefix"]
    """<p> The key prefix shared by all S3 Objects that are being imported. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3BucketSource) -> dict:
    out: dict = {}
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3BucketSource:
    out: S3BucketSource = {}  # type: ignore[typeddict-item]
    if "S3BucketOwner" in data:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("S3BucketSource.s3_bucket required")
    if "S3KeyPrefix" in data:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
