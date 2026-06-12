"""Generated from Smithy shape ``com.amazonaws.mpa#Operator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

Operator: TypeAlias = Literal[
    "EQ",
    "NE",
    "GT",
    "LT",
    "GTE",
    "LTE",
    "CONTAINS",
    "NOT_CONTAINS",
    "BETWEEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "NE",
        "GT",
        "LT",
        "GTE",
        "LTE",
        "CONTAINS",
        "NOT_CONTAINS",
        "BETWEEN",
    )
)


def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operator value: {data!r}")
    return cast(Operator, data)
