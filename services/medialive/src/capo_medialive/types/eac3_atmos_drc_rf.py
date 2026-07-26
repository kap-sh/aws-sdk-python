"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3AtmosDrcRf``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Atmos Drc Rf"""
Eac3AtmosDrcRf: TypeAlias = Literal[
    "FILM_LIGHT",
    "FILM_STANDARD",
    "MUSIC_LIGHT",
    "MUSIC_STANDARD",
    "NONE",
    "SPEECH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosDrcRf) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosDrcRf:
    return cast(Eac3AtmosDrcRf, data)
