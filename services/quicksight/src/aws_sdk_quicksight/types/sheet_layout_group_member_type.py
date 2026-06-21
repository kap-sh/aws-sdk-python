"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutGroupMemberType``."""

from typing import Literal, TypeAlias, cast

SheetLayoutGroupMemberType: TypeAlias = Literal[
    "ELEMENT",
    "GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetLayoutGroupMemberType) -> str:
    return value


def deserialize_json(data: str) -> SheetLayoutGroupMemberType:
    return cast(SheetLayoutGroupMemberType, data)
