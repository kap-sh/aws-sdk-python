"""Generated from Smithy shape ``com.amazonaws.quicksight#ConstantType``."""

from typing import Literal, TypeAlias, cast

ConstantType: TypeAlias = Literal[
    "SINGULAR",
    "RANGE",
    "COLLECTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConstantType) -> str:
    return value


def deserialize_json(data: str) -> ConstantType:
    return cast(ConstantType, data)
