"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcThickness``."""

from typing import Literal, TypeAlias, cast

ArcThickness: TypeAlias = Literal[
    "SMALL",
    "MEDIUM",
    "LARGE",
    "WHOLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArcThickness) -> str:
    return value


def deserialize_json(data: str) -> ArcThickness:
    return cast(ArcThickness, data)
