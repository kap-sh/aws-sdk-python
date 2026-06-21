"""Generated from Smithy shape ``com.amazonaws.macie2#BucketMetadataErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The code for an error or issue that prevented Amazon Macie from retrieving and processing information about an S3 bucket and the bucket's objects.</p>"""
BucketMetadataErrorCode: TypeAlias = Literal[
    "ACCESS_DENIED",
    "BUCKET_COUNT_EXCEEDS_QUOTA",
]


# --- restJson1 ser/de ---
def serialize_json(value: BucketMetadataErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BucketMetadataErrorCode:
    return cast(BucketMetadataErrorCode, data)
