"""Generated from Smithy shape ``com.amazonaws.qbusiness#StringAttributeValueBoostingLevel``."""

from typing import Literal, TypeAlias, cast

StringAttributeValueBoostingLevel: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "VERY_HIGH",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StringAttributeValueBoostingLevel) -> str:
    return value


def deserialize_json(data: str) -> StringAttributeValueBoostingLevel:
    return cast(StringAttributeValueBoostingLevel, data)
