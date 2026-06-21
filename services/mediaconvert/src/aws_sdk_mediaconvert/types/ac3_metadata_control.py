"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac3MetadataControl``."""

from typing import Literal, TypeAlias, cast

"""When set to FOLLOW_INPUT, encoder metadata will be sourced from the DD, DD+, or DolbyE decoder that supplied this audio data. If audio was not supplied from one of these streams, then the static metadata settings will be used."""
Ac3MetadataControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac3MetadataControl) -> str:
    return value


def deserialize_json(data: str) -> Ac3MetadataControl:
    return cast(Ac3MetadataControl, data)
