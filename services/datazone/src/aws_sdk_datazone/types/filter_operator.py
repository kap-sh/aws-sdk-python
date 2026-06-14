"""Generated from Smithy shape ``com.amazonaws.datazone#FilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

FilterOperator: TypeAlias = Literal[
    "EQ",
    "LE",
    "LT",
    "GE",
    "GT",
    "TEXT_SEARCH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "LE",
        "LT",
        "GE",
        "GT",
        "TEXT_SEARCH",
    )
)


def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterOperator value: {data!r}")
    return cast(FilterOperator, data)
