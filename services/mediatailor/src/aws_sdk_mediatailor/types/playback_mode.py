"""Generated from Smithy shape ``com.amazonaws.mediatailor#PlaybackMode``."""

from typing import Literal, TypeAlias, cast

PlaybackMode: TypeAlias = Literal[
    "LOOP",
    "LINEAR",
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackMode) -> str:
    return value


def deserialize_json(data: str) -> PlaybackMode:
    return cast(PlaybackMode, data)
