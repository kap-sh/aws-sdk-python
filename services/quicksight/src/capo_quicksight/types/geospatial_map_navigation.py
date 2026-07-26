"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapNavigation``."""

from typing import Literal, TypeAlias, cast

GeospatialMapNavigation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapNavigation) -> str:
    return value


def deserialize_json(data: str) -> GeospatialMapNavigation:
    return cast(GeospatialMapNavigation, data)
