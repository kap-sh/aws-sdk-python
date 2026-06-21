"""Generated from Smithy shape ``com.amazonaws.groundstation#Polarization``."""

from typing import Literal, TypeAlias, cast

Polarization: TypeAlias = Literal[
    "RIGHT_HAND",
    "LEFT_HAND",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Polarization) -> str:
    return value


def deserialize_json(data: str) -> Polarization:
    return cast(Polarization, data)
