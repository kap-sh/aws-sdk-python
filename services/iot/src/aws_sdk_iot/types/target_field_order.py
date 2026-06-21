"""Generated from Smithy shape ``com.amazonaws.iot#TargetFieldOrder``."""

from typing import Literal, TypeAlias, cast

TargetFieldOrder: TypeAlias = Literal[
    "LatLon",
    "LonLat",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetFieldOrder) -> str:
    return value


def deserialize_json(data: str) -> TargetFieldOrder:
    return cast(TargetFieldOrder, data)
