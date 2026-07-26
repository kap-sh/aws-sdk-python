"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#TileOrder``."""

from typing import Literal, TypeAlias, cast

TileOrder: TypeAlias = Literal[
    "JoinSequence",
    "SpeakerSequence",
]


# --- restJson1 ser/de ---
def serialize_json(value: TileOrder) -> str:
    return value


def deserialize_json(data: str) -> TileOrder:
    return cast(TileOrder, data)
