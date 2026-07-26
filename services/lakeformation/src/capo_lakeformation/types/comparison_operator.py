"""Generated from Smithy shape ``com.amazonaws.lakeformation#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
