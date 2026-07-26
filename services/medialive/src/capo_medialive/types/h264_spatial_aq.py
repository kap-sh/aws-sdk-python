"""Generated from Smithy shape ``com.amazonaws.medialive#H264SpatialAq``."""

from typing import Literal, TypeAlias, cast

"""H264 Spatial Aq"""
H264SpatialAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264SpatialAq) -> str:
    return value


def deserialize_json(data: str) -> H264SpatialAq:
    return cast(H264SpatialAq, data)
