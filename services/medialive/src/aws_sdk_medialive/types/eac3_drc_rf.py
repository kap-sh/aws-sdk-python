"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3DrcRf``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "FILM_LIGHT",
        "FILM_STANDARD",
        "MUSIC_LIGHT",
        "MUSIC_STANDARD",
        "NONE",
        "SPEECH",
    )
)


def serialize_json(value: Eac3DrcRf) -> str:
    return value


def deserialize_json(data: str) -> Eac3DrcRf:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3DrcRf value: {data!r}")
    return cast(Eac3DrcRf, data)
