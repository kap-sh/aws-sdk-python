"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsNielsenId3``."""

from typing import Literal, TypeAlias, cast

"""If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
M2tsNielsenId3: TypeAlias = Literal[
    "INSERT",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsNielsenId3) -> str:
    return value


def deserialize_json(data: str) -> M2tsNielsenId3:
    return cast(M2tsNielsenId3, data)
