"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeGranularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TimeGranularity: TypeAlias = Literal[
    "YEAR",
    "QUARTER",
    "MONTH",
    "WEEK",
    "DAY",
    "HOUR",
    "MINUTE",
    "SECOND",
    "MILLISECOND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YEAR",
        "QUARTER",
        "MONTH",
        "WEEK",
        "DAY",
        "HOUR",
        "MINUTE",
        "SECOND",
        "MILLISECOND",
    )
)


def serialize_json(value: TimeGranularity) -> str:
    return value


def deserialize_json(data: str) -> TimeGranularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeGranularity value: {data!r}")
    return cast(TimeGranularity, data)
