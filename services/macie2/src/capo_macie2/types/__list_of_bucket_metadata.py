"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfBucketMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.bucket_metadata

__listOfBucketMetadata: TypeAlias = list[
    "capo_macie2.types.bucket_metadata.BucketMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBucketMetadata) -> list:
    import capo_macie2.types.bucket_metadata

    out: list = []
    for item in value:
        out.append(capo_macie2.types.bucket_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBucketMetadata:
    import capo_macie2.types.bucket_metadata

    out: __listOfBucketMetadata = []
    for item in data:
        out.append(capo_macie2.types.bucket_metadata.deserialize_json(item))
    return out
