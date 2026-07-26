"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeBoostingLevel``."""

from typing import Literal, TypeAlias, cast

DocumentAttributeBoostingLevel: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
    "VERY_HIGH",
    "ONE",
    "TWO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeBoostingLevel) -> str:
    return value


def deserialize_json(data: str) -> DocumentAttributeBoostingLevel:
    return cast(DocumentAttributeBoostingLevel, data)
