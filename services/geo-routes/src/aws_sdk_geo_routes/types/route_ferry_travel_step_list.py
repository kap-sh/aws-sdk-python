"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_ferry_travel_step

RouteFerryTravelStepList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_ferry_travel_step.RouteFerryTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryTravelStepList) -> list:
    import aws_sdk_geo_routes.types.route_ferry_travel_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_ferry_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteFerryTravelStepList:
    import aws_sdk_geo_routes.types.route_ferry_travel_step

    out: RouteFerryTravelStepList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_ferry_travel_step.deserialize_json(item)
        )
    return out
