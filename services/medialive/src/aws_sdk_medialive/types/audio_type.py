"""Generated from Smithy shape ``com.amazonaws.medialive#AudioType``."""

from typing import Literal, TypeAlias, cast

"""Audio Type"""
AudioType: TypeAlias = Literal[
    "CLEAN_EFFECTS",
    "HEARING_IMPAIRED",
    "UNDEFINED",
    "VISUAL_IMPAIRED_COMMENTARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioType) -> str:
    return value


def deserialize_json(data: str) -> AudioType:
    return cast(AudioType, data)
