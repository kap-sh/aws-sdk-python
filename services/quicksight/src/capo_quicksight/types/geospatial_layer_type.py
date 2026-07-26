"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerType``."""

from typing import Literal, TypeAlias, cast

GeospatialLayerType: TypeAlias = Literal[
    "POINT",
    "LINE",
    "POLYGON",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerType) -> str:
    return value


def deserialize_json(data: str) -> GeospatialLayerType:
    return cast(GeospatialLayerType, data)
