"""Generated from Smithy shape ``com.amazonaws.qbusiness#NumberAttributeBoostingType``."""

from typing import Literal, TypeAlias, cast

NumberAttributeBoostingType: TypeAlias = Literal[
    "PRIORITIZE_LARGER_VALUES",
    "PRIORITIZE_SMALLER_VALUES",
]


# --- restJson1 ser/de ---
def serialize_json(value: NumberAttributeBoostingType) -> str:
    return value


def deserialize_json(data: str) -> NumberAttributeBoostingType:
    return cast(NumberAttributeBoostingType, data)
