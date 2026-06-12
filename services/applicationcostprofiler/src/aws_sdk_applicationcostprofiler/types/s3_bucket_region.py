"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#S3BucketRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_applicationcostprofiler.errors import DeserializationError

S3BucketRegion: TypeAlias = Literal[
    "ap-east-1",
    "me-south-1",
    "eu-south-1",
    "af-south-1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ap-east-1",
        "me-south-1",
        "eu-south-1",
        "af-south-1",
    )
)


def serialize_json(value: S3BucketRegion) -> str:
    return value


def deserialize_json(data: str) -> S3BucketRegion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3BucketRegion value: {data!r}")
    return cast(S3BucketRegion, data)
