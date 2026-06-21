"""Generated from Smithy shape ``com.amazonaws.mediaconvert#S3StorageClass``."""

from typing import Literal, TypeAlias, cast

"""Specify the S3 storage class to use for this output. To use your destination's default storage class: Keep the default value, Not set. For more information about S3 storage classes, see https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"""
S3StorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "STANDARD_IA",
    "ONEZONE_IA",
    "INTELLIGENT_TIERING",
    "GLACIER",
    "DEEP_ARCHIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3StorageClass) -> str:
    return value


def deserialize_json(data: str) -> S3StorageClass:
    return cast(S3StorageClass, data)
