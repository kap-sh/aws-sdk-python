"""Generated from Smithy shape ``com.amazonaws.connect#DateTimeComparisonType``."""

from typing import Literal, TypeAlias, cast

DateTimeComparisonType: TypeAlias = Literal[
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN_OR_EQUAL_TO",
    "EQUAL_TO",
    "RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeComparisonType) -> str:
    return value


def deserialize_json(data: str) -> DateTimeComparisonType:
    return cast(DateTimeComparisonType, data)
