"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoricalAggregationFunction``."""

from typing import Literal, TypeAlias, cast

CategoricalAggregationFunction: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoricalAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> CategoricalAggregationFunction:
    return cast(CategoricalAggregationFunction, data)
