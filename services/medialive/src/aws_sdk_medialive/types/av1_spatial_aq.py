"""Generated from Smithy shape ``com.amazonaws.medialive#Av1SpatialAq``."""

from typing import Literal, TypeAlias, cast

"""Av1 Spatial Aq"""
Av1SpatialAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1SpatialAq) -> str:
    return value


def deserialize_json(data: str) -> Av1SpatialAq:
    return cast(Av1SpatialAq, data)
