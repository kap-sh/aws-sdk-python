"""Generated from Smithy shape ``com.amazonaws.quicksight#DateAggregationFunction``."""

from typing import Literal, TypeAlias, cast

DateAggregationFunction: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
    "MIN",
    "MAX",
]


# --- restJson1 ser/de ---
def serialize_json(value: DateAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> DateAggregationFunction:
    return cast(DateAggregationFunction, data)
