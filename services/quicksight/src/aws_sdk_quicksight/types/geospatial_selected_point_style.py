"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialSelectedPointStyle``."""

from typing import Literal, TypeAlias, cast

GeospatialSelectedPointStyle: TypeAlias = Literal[
    "POINT",
    "CLUSTER",
    "HEATMAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialSelectedPointStyle) -> str:
    return value


def deserialize_json(data: str) -> GeospatialSelectedPointStyle:
    return cast(GeospatialSelectedPointStyle, data)
