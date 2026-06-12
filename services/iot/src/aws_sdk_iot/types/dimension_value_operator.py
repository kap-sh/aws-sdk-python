"""Generated from Smithy shape ``com.amazonaws.iot#DimensionValueOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DimensionValueOperator: TypeAlias = Literal[
    "IN",
    "NOT_IN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN",
        "NOT_IN",
    )
)


def serialize_json(value: DimensionValueOperator) -> str:
    return value


def deserialize_json(data: str) -> DimensionValueOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionValueOperator value: {data!r}")
    return cast(DimensionValueOperator, data)
