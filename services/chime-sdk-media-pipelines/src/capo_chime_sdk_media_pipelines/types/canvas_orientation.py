"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CanvasOrientation``."""

from typing import Literal, TypeAlias, cast

CanvasOrientation: TypeAlias = Literal[
    "Landscape",
    "Portrait",
]


# --- restJson1 ser/de ---
def serialize_json(value: CanvasOrientation) -> str:
    return value


def deserialize_json(data: str) -> CanvasOrientation:
    return cast(CanvasOrientation, data)
