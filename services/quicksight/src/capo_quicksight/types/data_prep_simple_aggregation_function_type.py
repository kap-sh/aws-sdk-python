"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepSimpleAggregationFunctionType``."""

from typing import Literal, TypeAlias, cast

DataPrepSimpleAggregationFunctionType: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
    "SUM",
    "AVERAGE",
    "MAX",
    "MIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataPrepSimpleAggregationFunctionType) -> str:
    return value


def deserialize_json(data: str) -> DataPrepSimpleAggregationFunctionType:
    return cast(DataPrepSimpleAggregationFunctionType, data)
