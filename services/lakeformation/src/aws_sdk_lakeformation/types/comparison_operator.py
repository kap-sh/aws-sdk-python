"""Generated from Smithy shape ``com.amazonaws.lakeformation#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "EQ",
    "NE",
    "LE",
    "LT",
    "GE",
    "GT",
    "CONTAINS",
    "NOT_CONTAINS",
    "BEGINS_WITH",
    "IN",
    "BETWEEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "NE",
        "LE",
        "LT",
        "GE",
        "GT",
        "CONTAINS",
        "NOT_CONTAINS",
        "BEGINS_WITH",
        "IN",
        "BETWEEN",
    )
)


def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
