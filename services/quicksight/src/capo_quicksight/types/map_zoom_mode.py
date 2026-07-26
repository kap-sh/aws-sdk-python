"""Generated from Smithy shape ``com.amazonaws.quicksight#MapZoomMode``."""

from typing import Literal, TypeAlias, cast

MapZoomMode: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MapZoomMode) -> str:
    return value


def deserialize_json(data: str) -> MapZoomMode:
    return cast(MapZoomMode, data)
