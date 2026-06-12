"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfS3BucketName``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.s3_bucket_name

__listOfS3BucketName: TypeAlias = list[
    "aws_sdk_macie2.types.s3_bucket_name.S3BucketName"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfS3BucketName) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOfS3BucketName:
    return list(data)
