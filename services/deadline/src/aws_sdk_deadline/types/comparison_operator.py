"""Generated from Smithy shape ``com.amazonaws.deadline#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

ComparisonOperator: TypeAlias = Literal[
    "EQUAL",
    "NOT_EQUAL",
    "GREATER_THAN_EQUAL_TO",
    "GREATER_THAN",
    "LESS_THAN_EQUAL_TO",
    "LESS_THAN",
    "ANY_EQUALS",
    "ALL_NOT_EQUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
