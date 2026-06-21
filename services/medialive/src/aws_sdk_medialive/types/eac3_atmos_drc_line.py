"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3AtmosDrcLine``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Atmos Drc Line"""
Eac3AtmosDrcLine: TypeAlias = Literal[
    "FILM_LIGHT",
    "FILM_STANDARD",
    "MUSIC_LIGHT",
    "MUSIC_STANDARD",
    "NONE",
    "SPEECH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosDrcLine) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDrcLine:
    return cast(Eac3AtmosDrcLine, data)
