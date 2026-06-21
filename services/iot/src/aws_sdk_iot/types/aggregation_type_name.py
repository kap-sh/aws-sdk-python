"""Generated from Smithy shape ``com.amazonaws.iot#AggregationTypeName``."""

from typing import Literal, TypeAlias, cast

AggregationTypeName: TypeAlias = Literal[
    "Statistics",
    "Percentiles",
    "Cardinality",
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationTypeName) -> str:
    return value


def deserialize_json(data: str) -> AggregationTypeName:
    return cast(AggregationTypeName, data)
