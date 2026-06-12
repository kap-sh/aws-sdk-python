"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentModerationSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

ContentModerationSortBy: TypeAlias = Literal[
    "NAME",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "TIMESTAMP",
    )
)


def serialize_aws_json_1_1(value: ContentModerationSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentModerationSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentModerationSortBy value: {data!r}")
    return cast(ContentModerationSortBy, data)
