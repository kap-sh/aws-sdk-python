"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac3BitstreamMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the bitstream mode for the AC-3 stream that the encoder emits. For more information about the AC3 bitstream mode, see ATSC A/52-2012 (Annex E)."""
Ac3BitstreamMode: TypeAlias = Literal[
    "COMPLETE_MAIN",
    "COMMENTARY",
    "DIALOGUE",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "MUSIC_AND_EFFECTS",
    "VISUALLY_IMPAIRED",
    "VOICE_OVER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE_MAIN",
        "COMMENTARY",
        "DIALOGUE",
        "EMERGENCY",
        "HEARING_IMPAIRED",
        "MUSIC_AND_EFFECTS",
        "VISUALLY_IMPAIRED",
        "VOICE_OVER",
    )
)


def serialize_json(value: Ac3BitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Ac3BitstreamMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ac3BitstreamMode value: {data!r}")
    return cast(Ac3BitstreamMode, data)
