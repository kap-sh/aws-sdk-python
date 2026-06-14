"""Generated from Smithy shape ``com.amazonaws.datazone#FilterExpressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

FilterExpressionType: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: FilterExpressionType) -> str:
    return value


def deserialize_json(data: str) -> FilterExpressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterExpressionType value: {data!r}")
    return cast(FilterExpressionType, data)
