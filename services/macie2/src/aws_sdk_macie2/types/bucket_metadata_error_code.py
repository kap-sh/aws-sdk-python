"""Generated from Smithy shape ``com.amazonaws.macie2#BucketMetadataErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The code for an error or issue that prevented Amazon Macie from retrieving and processing information about an S3 bucket and the bucket's objects.</p>"""
BucketMetadataErrorCode: TypeAlias = Literal[
    "ACCESS_DENIED",
    "BUCKET_COUNT_EXCEEDS_QUOTA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "BUCKET_COUNT_EXCEEDS_QUOTA",
    )
)


def serialize_json(value: BucketMetadataErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BucketMetadataErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BucketMetadataErrorCode value: {data!r}")
    return cast(BucketMetadataErrorCode, data)
