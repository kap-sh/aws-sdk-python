"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultAggregation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DefaultAggregation: TypeAlias = Literal[
    "SUM",
    "MAX",
    "MIN",
    "COUNT",
    "DISTINCT_COUNT",
    "AVERAGE",
    "MEDIAN",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUM",
        "MAX",
        "MIN",
        "COUNT",
        "DISTINCT_COUNT",
        "AVERAGE",
        "MEDIAN",
        "STDEV",
        "STDEVP",
        "VAR",
        "VARP",
    )
)


def serialize_json(value: DefaultAggregation) -> str:
    return value


def deserialize_json(data: str) -> DefaultAggregation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultAggregation value: {data!r}")
    return cast(DefaultAggregation, data)
