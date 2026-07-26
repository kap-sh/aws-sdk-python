"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VerticalTilePosition``."""

from typing import Literal, TypeAlias, cast

VerticalTilePosition: TypeAlias = Literal[
    "Left",
    "Right",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerticalTilePosition) -> str:
    return value


def deserialize_json(data: str) -> VerticalTilePosition:
    return cast(VerticalTilePosition, data)
