"""Generated from Smithy shape ``com.amazonaws.connect#DateComparisonType``."""

from typing import Literal, TypeAlias, cast

DateComparisonType: TypeAlias = Literal[
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN_OR_EQUAL_TO",
    "EQUAL_TO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DateComparisonType) -> str:
    return value


def deserialize_json(data: str) -> DateComparisonType:
    return cast(DateComparisonType, data)
