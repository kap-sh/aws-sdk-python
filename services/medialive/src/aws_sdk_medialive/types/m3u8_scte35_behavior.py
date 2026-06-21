"""Generated from Smithy shape ``com.amazonaws.medialive#M3u8Scte35Behavior``."""

from typing import Literal, TypeAlias, cast

"""M3u8 Scte35 Behavior"""
M3u8Scte35Behavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M3u8Scte35Behavior) -> str:
    return value


def deserialize_json(data: str) -> M3u8Scte35Behavior:
    return cast(M3u8Scte35Behavior, data)
