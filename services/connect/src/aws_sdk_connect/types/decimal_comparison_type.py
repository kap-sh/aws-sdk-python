"""Generated from Smithy shape ``com.amazonaws.connect#DecimalComparisonType``."""

from typing import Literal, TypeAlias, cast

DecimalComparisonType: TypeAlias = Literal[
    "GREATER_OR_EQUAL",
    "GREATER",
    "LESSER_OR_EQUAL",
    "LESSER",
    "EQUAL",
    "NOT_EQUAL",
    "RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalComparisonType) -> str:
    return value


def deserialize_json(data: str) -> DecimalComparisonType:
    return cast(DecimalComparisonType, data)
