"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsEbpPlacement``."""

from typing import Literal, TypeAlias, cast

"""M2ts Ebp Placement"""
M2tsEbpPlacement: TypeAlias = Literal[
    "VIDEO_AND_AUDIO_PIDS",
    "VIDEO_PID",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsEbpPlacement) -> str:
    return value


def deserialize_json(data: str) -> M2tsEbpPlacement:
    return cast(M2tsEbpPlacement, data)
