"""Generated from Smithy shape ``com.amazonaws.iot#AggregationTypeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AggregationTypeName: TypeAlias = Literal[
    "Statistics",
    "Percentiles",
    "Cardinality",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Statistics",
        "Percentiles",
        "Cardinality",
    )
)


def serialize_json(value: AggregationTypeName) -> str:
    return value


def deserialize_json(data: str) -> AggregationTypeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregationTypeName value: {data!r}")
    return cast(AggregationTypeName, data)
