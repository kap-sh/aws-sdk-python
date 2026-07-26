"""Generated from Smithy shape ``com.amazonaws.connect#NumberComparisonType``."""

from typing import Literal, TypeAlias, cast

NumberComparisonType: TypeAlias = Literal[
    "GREATER_OR_EQUAL",
    "GREATER",
    "LESSER_OR_EQUAL",
    "LESSER",
    "EQUAL",
    "NOT_EQUAL",
    "RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NumberComparisonType) -> str:
    return value


def deserialize_json(data: str) -> NumberComparisonType:
    return cast(NumberComparisonType, data)
