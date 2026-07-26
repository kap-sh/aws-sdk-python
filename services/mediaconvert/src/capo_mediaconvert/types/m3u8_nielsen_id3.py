"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M3u8NielsenId3``."""

from typing import Literal, TypeAlias, cast

"""If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
M3u8NielsenId3: TypeAlias = Literal[
    "INSERT",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M3u8NielsenId3) -> str:
    return value


def deserialize_json(data: str) -> M3u8NielsenId3:
    return cast(M3u8NielsenId3, data)
