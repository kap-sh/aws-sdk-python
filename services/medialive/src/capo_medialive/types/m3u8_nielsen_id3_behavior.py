"""Generated from Smithy shape ``com.amazonaws.medialive#M3u8NielsenId3Behavior``."""

from typing import Literal, TypeAlias, cast

"""M3u8 Nielsen Id3 Behavior"""
M3u8NielsenId3Behavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M3u8NielsenId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> M3u8NielsenId3Behavior:
    return cast(M3u8NielsenId3Behavior, data)
