"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleTotalAggregationFunction``."""

from typing import Literal, TypeAlias, cast

SimpleTotalAggregationFunction: TypeAlias = Literal[
    "DEFAULT",
    "SUM",
    "AVERAGE",
    "MIN",
    "MAX",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SimpleTotalAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> SimpleTotalAggregationFunction:
    return cast(SimpleTotalAggregationFunction, data)
