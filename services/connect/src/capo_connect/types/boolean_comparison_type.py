"""Generated from Smithy shape ``com.amazonaws.connect#BooleanComparisonType``."""

from typing import Literal, TypeAlias, cast

BooleanComparisonType: TypeAlias = Literal[
    "IS_TRUE",
    "IS_FALSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BooleanComparisonType) -> str:
    return value


def deserialize_json(data: str) -> BooleanComparisonType:
    return cast(BooleanComparisonType, data)
