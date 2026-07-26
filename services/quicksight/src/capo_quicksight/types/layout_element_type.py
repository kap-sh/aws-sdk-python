"""Generated from Smithy shape ``com.amazonaws.quicksight#LayoutElementType``."""

from typing import Literal, TypeAlias, cast

LayoutElementType: TypeAlias = Literal[
    "VISUAL",
    "FILTER_CONTROL",
    "PARAMETER_CONTROL",
    "TEXT_BOX",
    "IMAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutElementType) -> str:
    return value


def deserialize_json(data: str) -> LayoutElementType:
    return cast(LayoutElementType, data)
