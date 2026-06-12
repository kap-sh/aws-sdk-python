"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianAfterTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_pedestrian_after_travel_step

RoutePedestrianAfterTravelStepList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_pedestrian_after_travel_step.RoutePedestrianAfterTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianAfterTravelStepList) -> list:
    import aws_sdk_geo_routes.types.route_pedestrian_after_travel_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_pedestrian_after_travel_step.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RoutePedestrianAfterTravelStepList:
    import aws_sdk_geo_routes.types.route_pedestrian_after_travel_step

    out: RoutePedestrianAfterTravelStepList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_pedestrian_after_travel_step.deserialize_json(
                item
            )
        )
    return out
