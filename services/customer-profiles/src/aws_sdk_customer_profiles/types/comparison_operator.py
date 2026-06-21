"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
    "CONTAINS",
    "BEGINS_WITH",
    "ENDS_WITH",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN_OR_EQUAL",
    "EQUAL",
    "BEFORE",
    "AFTER",
    "ON",
    "BETWEEN",
    "NOT_BETWEEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
