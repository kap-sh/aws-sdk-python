"""Generated from Smithy shape ``com.amazonaws.appflow#Operators``."""

from typing import Literal, TypeAlias, cast

Operators: TypeAlias = Literal[
    "PROJECTION",
    "LESS_THAN",
    "GREATER_THAN",
    "CONTAINS",
    "BETWEEN",
    "LESS_THAN_OR_EQUAL_TO",
    "GREATER_THAN_OR_EQUAL_TO",
    "EQUAL_TO",
    "NOT_EQUAL_TO",
    "ADDITION",
    "MULTIPLICATION",
    "DIVISION",
    "SUBTRACTION",
    "MASK_ALL",
    "MASK_FIRST_N",
    "MASK_LAST_N",
    "VALIDATE_NON_NULL",
    "VALIDATE_NON_ZERO",
    "VALIDATE_NON_NEGATIVE",
    "VALIDATE_NUMERIC",
    "NO_OP",
]


# --- restJson1 ser/de ---
def serialize_json(value: Operators) -> str:
    return value


def deserialize_json(data: str) -> Operators:
    return cast(Operators, data)
