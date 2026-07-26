"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3DrcLine``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Drc Line"""
Eac3DrcLine: TypeAlias = Literal[
    "FILM_LIGHT",
    "FILM_STANDARD",
    "MUSIC_LIGHT",
    "MUSIC_STANDARD",
    "NONE",
    "SPEECH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3DrcLine) -> str:
    return value


def deserialize_json(data: str) -> Eac3DrcLine:
    return cast(Eac3DrcLine, data)
