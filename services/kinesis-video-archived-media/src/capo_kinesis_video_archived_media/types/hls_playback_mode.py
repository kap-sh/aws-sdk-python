"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSPlaybackMode``."""

from typing import Literal, TypeAlias, cast

HLSPlaybackMode: TypeAlias = Literal[
    "LIVE",
    "LIVE_REPLAY",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
def serialize_json(value: HLSPlaybackMode) -> str:
    return value


def deserialize_json(data: str) -> HLSPlaybackMode:
    return cast(HLSPlaybackMode, data)
