"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleAttributeAggregationFunction``."""

from typing import Literal, TypeAlias, cast

SimpleAttributeAggregationFunction: TypeAlias = Literal["UNIQUE_VALUE",]


# --- restJson1 ser/de ---
def serialize_json(value: SimpleAttributeAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> SimpleAttributeAggregationFunction:
    return cast(SimpleAttributeAggregationFunction, data)
