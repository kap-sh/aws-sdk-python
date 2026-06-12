"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3BitstreamMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "COMMENTARY",
        "COMPLETE_MAIN",
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
