"""Generated from Smithy shape ``com.amazonaws.georoutes#PolylineRingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.polyline_ring

PolylineRingList: TypeAlias = list[
    "aws_sdk_geo_routes.types.polyline_ring.PolylineRing"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolylineRingList) -> list:
    return list(value)


def deserialize_json(data: list) -> PolylineRingList:
    return list(data)
