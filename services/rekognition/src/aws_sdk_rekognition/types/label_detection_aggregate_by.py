"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionAggregateBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

LabelDetectionAggregateBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: LabelDetectionAggregateBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelDetectionAggregateBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LabelDetectionAggregateBy value: {data!r}")
    return cast(LabelDetectionAggregateBy, data)
