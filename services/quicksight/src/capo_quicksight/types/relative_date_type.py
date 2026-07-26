"""Generated from Smithy shape ``com.amazonaws.quicksight#RelativeDateType``."""

from typing import Literal, TypeAlias, cast

RelativeDateType: TypeAlias = Literal[
    "PREVIOUS",
    "THIS",
    "LAST",
    "NOW",
    "NEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RelativeDateType) -> str:
    return value


def deserialize_json(data: str) -> RelativeDateType:
    return cast(RelativeDateType, data)
