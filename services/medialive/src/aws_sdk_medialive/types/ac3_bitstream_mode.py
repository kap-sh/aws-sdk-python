"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3BitstreamMode``."""

from typing import Literal, TypeAlias, cast

"""Ac3 Bitstream Mode"""
Ac3BitstreamMode: TypeAlias = Literal[
    "COMMENTARY",
    "COMPLETE_MAIN",
    "DIALOGUE",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "MUSIC_AND_EFFECTS",
    "VISUALLY_IMPAIRED",
    "VOICE_OVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3BitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Ac3BitstreamMode:
    return cast(Ac3BitstreamMode, data)
