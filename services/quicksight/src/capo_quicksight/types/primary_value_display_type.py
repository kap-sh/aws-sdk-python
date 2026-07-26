"""Generated from Smithy shape ``com.amazonaws.quicksight#PrimaryValueDisplayType``."""

from typing import Literal, TypeAlias, cast

PrimaryValueDisplayType: TypeAlias = Literal[
    "HIDDEN",
    "COMPARISON",
    "ACTUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryValueDisplayType) -> str:
    return value


def deserialize_json(data: str) -> PrimaryValueDisplayType:
    return cast(PrimaryValueDisplayType, data)
