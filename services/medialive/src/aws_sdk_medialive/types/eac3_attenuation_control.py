"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3AttenuationControl``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Attenuation Control"""
Eac3AttenuationControl: TypeAlias = Literal[
    "ATTENUATE_3_DB",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AttenuationControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3AttenuationControl:
    return cast(Eac3AttenuationControl, data)
