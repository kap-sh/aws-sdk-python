"""Generated from Smithy shape ``com.amazonaws.quicksight#DateAggregationFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DateAggregationFunction: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
    "MIN",
    "MAX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COUNT",
        "DISTINCT_COUNT",
        "MIN",
        "MAX",
    )
)


def serialize_json(value: DateAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> DateAggregationFunction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DateAggregationFunction value: {data!r}")
    return cast(DateAggregationFunction, data)
