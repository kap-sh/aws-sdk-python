"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#S3BucketRegion``."""

from typing import Literal, TypeAlias, cast

S3BucketRegion: TypeAlias = Literal[
    "ap-east-1",
    "me-south-1",
    "eu-south-1",
    "af-south-1",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketRegion) -> str:
    return value


def deserialize_json(data: str) -> S3BucketRegion:
    return cast(S3BucketRegion, data)
