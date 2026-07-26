"""Generated from Smithy shape ``com.amazonaws.medialive#Ac3MetadataControl``."""

from typing import Literal, TypeAlias, cast

"""Ac3 Metadata Control"""
Ac3MetadataControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3MetadataControl) -> str:
    return value


def deserialize_json(data: str) -> Ac3MetadataControl:
    return cast(Ac3MetadataControl, data)
