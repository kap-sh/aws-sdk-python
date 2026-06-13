"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepSimpleAggregationFunctionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataPrepSimpleAggregationFunctionType: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
    "SUM",
    "AVERAGE",
    "MAX",
    "MIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COUNT",
        "DISTINCT_COUNT",
        "SUM",
        "AVERAGE",
        "MAX",
        "MIN",
    )
)


def serialize_json(value: DataPrepSimpleAggregationFunctionType) -> str:
    return value


def deserialize_json(data: str) -> DataPrepSimpleAggregationFunctionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataPrepSimpleAggregationFunctionType value: {data!r}"
        )
    return cast(DataPrepSimpleAggregationFunctionType, data)
