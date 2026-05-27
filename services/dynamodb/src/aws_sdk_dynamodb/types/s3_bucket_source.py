"""Generated from Smithy shape ``com.amazonaws.dynamodb#S3BucketSource``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
