"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicTimeGranularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicTimeGranularity: TypeAlias = Literal[
    "SECOND",
    "MINUTE",
    "HOUR",
    "DAY",
    "WEEK",
    "MONTH",
    "QUARTER",
    "YEAR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECOND",
        "MINUTE",
        "HOUR",
        "DAY",
        "WEEK",
        "MONTH",
        "QUARTER",
        "YEAR",
    )
)


def serialize_json(value: TopicTimeGranularity) -> str:
    return value


def deserialize_json(data: str) -> TopicTimeGranularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicTimeGranularity value: {data!r}")
    return cast(TopicTimeGranularity, data)
