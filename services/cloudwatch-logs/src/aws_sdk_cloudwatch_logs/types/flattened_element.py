"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FlattenedElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

FlattenedElement: TypeAlias = Literal[
    "first",
    "last",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "first",
        "last",
    )
)


def serialize_aws_json_1_1(value: FlattenedElement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlattenedElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlattenedElement value: {data!r}")
    return cast(FlattenedElement, data)
