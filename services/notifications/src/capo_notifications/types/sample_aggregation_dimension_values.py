"""Generated from Smithy shape ``com.amazonaws.notifications#SampleAggregationDimensionValues``."""

from typing import TypeAlias

SampleAggregationDimensionValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SampleAggregationDimensionValues) -> list:
    return list(value)


def deserialize_json(data: list) -> SampleAggregationDimensionValues:
    return list(data)
