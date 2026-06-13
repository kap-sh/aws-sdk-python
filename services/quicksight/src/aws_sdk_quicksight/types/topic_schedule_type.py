"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicScheduleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicScheduleType: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
    )
)


def serialize_json(value: TopicScheduleType) -> str:
    return value


def deserialize_json(data: str) -> TopicScheduleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicScheduleType value: {data!r}")
    return cast(TopicScheduleType, data)
