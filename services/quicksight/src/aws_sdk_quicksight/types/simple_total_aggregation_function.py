"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleTotalAggregationFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SimpleTotalAggregationFunction: TypeAlias = Literal[
    "DEFAULT",
    "SUM",
    "AVERAGE",
    "MIN",
    "MAX",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "SUM",
        "AVERAGE",
        "MIN",
        "MAX",
        "NONE",
    )
)


def serialize_json(value: SimpleTotalAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> SimpleTotalAggregationFunction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SimpleTotalAggregationFunction value: {data!r}"
        )
    return cast(SimpleTotalAggregationFunction, data)
