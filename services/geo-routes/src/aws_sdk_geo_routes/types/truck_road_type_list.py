"""Generated from Smithy shape ``com.amazonaws.georoutes#TruckRoadTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.truck_road_type

TruckRoadTypeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.truck_road_type.TruckRoadType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TruckRoadTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> TruckRoadTypeList:
    return list(data)
