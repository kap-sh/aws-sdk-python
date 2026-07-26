"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3DrcProfile``."""

from typing import Literal, TypeAlias, cast

"""Ac3 Drc Profile"""
Ac3DrcProfile: TypeAlias = Literal[
    "FILM_STANDARD",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3DrcProfile) -> str:
    return value


def deserialize_json(data: str) -> Ac3DrcProfile:
    return cast(Ac3DrcProfile, data)
