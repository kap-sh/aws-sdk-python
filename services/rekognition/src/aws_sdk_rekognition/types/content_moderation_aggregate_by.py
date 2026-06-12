"""Generated from Smithy shape ``com.amazonaws.rekognition#ContentModerationAggregateBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

ContentModerationAggregateBy: TypeAlias = Literal[
    "TIMESTAMPS",
    "SEGMENTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TIMESTAMPS",
        "SEGMENTS",
    )
)


def serialize_aws_json_1_1(value: ContentModerationAggregateBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentModerationAggregateBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContentModerationAggregateBy value: {data!r}"
        )
    return cast(ContentModerationAggregateBy, data)
