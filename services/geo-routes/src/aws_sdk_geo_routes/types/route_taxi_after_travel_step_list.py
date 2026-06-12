"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiAfterTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_taxi_after_travel_step

RouteTaxiAfterTravelStepList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_taxi_after_travel_step.RouteTaxiAfterTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiAfterTravelStepList) -> list:
    import aws_sdk_geo_routes.types.route_taxi_after_travel_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_taxi_after_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTaxiAfterTravelStepList:
    import aws_sdk_geo_routes.types.route_taxi_after_travel_step

    out: RouteTaxiAfterTravelStepList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_taxi_after_travel_step.deserialize_json(item)
        )
    return out
