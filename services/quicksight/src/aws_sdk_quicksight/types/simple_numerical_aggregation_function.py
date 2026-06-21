"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleNumericalAggregationFunction``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SimpleNumericalAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> SimpleNumericalAggregationFunction:
    return cast(SimpleNumericalAggregationFunction, data)
