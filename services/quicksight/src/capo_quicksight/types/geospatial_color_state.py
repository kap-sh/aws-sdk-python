"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialColorState``."""

from typing import Literal, TypeAlias, cast

GeospatialColorState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialColorState) -> str:
    return value


def deserialize_json(data: str) -> GeospatialColorState:
    return cast(GeospatialColorState, data)
