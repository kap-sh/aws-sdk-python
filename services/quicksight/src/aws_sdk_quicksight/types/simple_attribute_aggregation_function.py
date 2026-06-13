"""Generated from Smithy shape ``com.amazonaws.quicksight#SimpleAttributeAggregationFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SimpleAttributeAggregationFunction: TypeAlias = Literal["UNIQUE_VALUE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UNIQUE_VALUE",))


def serialize_json(value: SimpleAttributeAggregationFunction) -> str:
    return value


def deserialize_json(data: str) -> SimpleAttributeAggregationFunction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SimpleAttributeAggregationFunction value: {data!r}"
        )
    return cast(SimpleAttributeAggregationFunction, data)
