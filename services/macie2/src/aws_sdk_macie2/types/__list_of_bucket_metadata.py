"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfBucketMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.bucket_metadata

__listOfBucketMetadata: TypeAlias = list[
    "aws_sdk_macie2.types.bucket_metadata.BucketMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBucketMetadata) -> list:
    import aws_sdk_macie2.types.bucket_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.bucket_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBucketMetadata:
    import aws_sdk_macie2.types.bucket_metadata

    out: __listOfBucketMetadata = []
    for item in data:
        out.append(aws_sdk_macie2.types.bucket_metadata.deserialize_json(item))
    return out
