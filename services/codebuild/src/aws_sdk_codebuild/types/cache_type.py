"""Generated from Smithy shape ``com.amazonaws.codebuild#CacheType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

CacheType: TypeAlias = Literal[
    "NO_CACHE",
    "S3",
    "LOCAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_CACHE",
        "S3",
        "LOCAL",
    )
)


def serialize_aws_json_1_1(value: CacheType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CacheType value: {data!r}")
    return cast(CacheType, data)
