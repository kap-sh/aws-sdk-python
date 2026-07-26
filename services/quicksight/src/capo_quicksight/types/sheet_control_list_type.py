"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlListType``."""

from typing import Literal, TypeAlias, cast

SheetControlListType: TypeAlias = Literal[
    "MULTI_SELECT",
    "SINGLE_SELECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlListType) -> str:
    return value


def deserialize_json(data: str) -> SheetControlListType:
    return cast(SheetControlListType, data)
