"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3MetadataControl``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Metadata Control"""
Eac3MetadataControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3MetadataControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3MetadataControl:
    return cast(Eac3MetadataControl, data)
