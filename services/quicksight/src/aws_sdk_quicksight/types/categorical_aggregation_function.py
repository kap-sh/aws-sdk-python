"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoricalAggregationFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CategoricalAggregationFunction: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COUNT",
        "DISTINCT_COUNT",
    )
)


def serialize_json(value: CategoricalAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> CategoricalAggregationFunction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CategoricalAggregationFunction value: {data!r}"
        )
    return cast(CategoricalAggregationFunction, data)
