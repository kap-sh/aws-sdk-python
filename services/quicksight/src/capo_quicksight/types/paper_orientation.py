"""Generated from Smithy shape ``com.amazonaws.quicksight#PaperOrientation``."""

from typing import Literal, TypeAlias, cast

PaperOrientation: TypeAlias = Literal[
    "PORTRAIT",
    "LANDSCAPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaperOrientation) -> str:
    return value


def deserialize_json(data: str) -> PaperOrientation:
    return cast(PaperOrientation, data)
