"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleNumericalAggregationFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SimpleNumericalAggregationFunction: TypeAlias = Literal[
    "SUM",
    "AVERAGE",
    "MIN",
    "MAX",
    "COUNT",
    "DISTINCT_COUNT",
    "VAR",
    "VARP",
    "STDEV",
    "STDEVP",
    "MEDIAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUM",
        "AVERAGE",
        "MIN",
        "MAX",
        "COUNT",
        "DISTINCT_COUNT",
        "VAR",
        "VARP",
        "STDEV",
        "STDEVP",
        "MEDIAN",
    )
)


def serialize_json(value: SimpleNumericalAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> SimpleNumericalAggregationFunction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SimpleNumericalAggregationFunction value: {data!r}"
        )
    return cast(SimpleNumericalAggregationFunction, data)
