"""Generated from Smithy shape ``com.amazonaws.connect#StringComparisonType``."""

from typing import Literal, TypeAlias, cast

StringComparisonType: TypeAlias = Literal[
    "STARTS_WITH",
    "CONTAINS",
    "EXACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: StringComparisonType) -> str:
    return value


def deserialize_json(data: str) -> StringComparisonType:
    return cast(StringComparisonType, data)
