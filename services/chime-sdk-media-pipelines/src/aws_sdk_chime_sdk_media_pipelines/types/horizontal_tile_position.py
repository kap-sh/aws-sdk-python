"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#HorizontalTilePosition``."""

from typing import Literal, TypeAlias, cast

HorizontalTilePosition: TypeAlias = Literal[
    "Top",
    "Bottom",
]


# --- restJson1 ser/de ---
def serialize_json(value: HorizontalTilePosition) -> str:
    return value


def deserialize_json(data: str) -> HorizontalTilePosition:
    return cast(HorizontalTilePosition, data)
