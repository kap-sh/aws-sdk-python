"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHPlaybackMode``."""

from typing import Literal, TypeAlias, cast

DASHPlaybackMode: TypeAlias = Literal[
    "LIVE",
    "LIVE_REPLAY",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
def serialize_json(value: DASHPlaybackMode) -> str:
    return value


def deserialize_json(data: str) -> DASHPlaybackMode:
    return cast(DASHPlaybackMode, data)
