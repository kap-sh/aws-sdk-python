"""Generated from Smithy shape ``com.amazonaws.georoutes#DistanceThresholdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters

DistanceThresholdList: TypeAlias = list[
    "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
]


# --- restJson1 ser/de ---
def serialize_json(value: DistanceThresholdList) -> list:
    return list(value)


def deserialize_json(data: list) -> DistanceThresholdList:
    return list(data)
