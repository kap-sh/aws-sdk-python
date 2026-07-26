"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3DrcRf``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Drc Rf"""
Eac3DrcRf: TypeAlias = Literal[
    "FILM_LIGHT",
    "FILM_STANDARD",
    "MUSIC_LIGHT",
    "MUSIC_STANDARD",
    "NONE",
    "SPEECH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3DrcRf) -> str:
    return value


def deserialize_json(data: str) -> Eac3DrcRf:
    return cast(Eac3DrcRf, data)
