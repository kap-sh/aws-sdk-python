"""Generated from Smithy shape ``com.amazonaws.mediapackage#PlaylistType``."""

from typing import Literal, TypeAlias, cast

PlaylistType: TypeAlias = Literal[
    "NONE",
    "EVENT",
    "VOD",
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaylistType) -> str:
    return value


def deserialize_json(data: str) -> PlaylistType:
    return cast(PlaylistType, data)
