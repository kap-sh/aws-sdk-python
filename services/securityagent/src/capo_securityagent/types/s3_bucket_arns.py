"""Generated from Smithy shape ``com.amazonaws.securityagent#S3BucketArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.s3_bucket_arn

S3BucketArns: TypeAlias = list["capo_securityagent.types.s3_bucket_arn.S3BucketArn"]


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketArns) -> list:
    return list(value)


def deserialize_json(data: list) -> S3BucketArns:
    return list(data)
