"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3AttenuationControl``."""

from typing import Literal, TypeAlias, cast

"""Ac3 Attenuation Control"""
Ac3AttenuationControl: TypeAlias = Literal[
    "ATTENUATE_3_DB",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3AttenuationControl) -> str:
    return value


def deserialize_json(data: str) -> Ac3AttenuationControl:
    return cast(Ac3AttenuationControl, data)
