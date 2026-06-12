"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_rental_travel_step

RouteRentalTravelStepList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_rental_travel_step.RouteRentalTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalTravelStepList) -> list:
    import aws_sdk_geo_routes.types.route_rental_travel_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_rental_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteRentalTravelStepList:
    import aws_sdk_geo_routes.types.route_rental_travel_step

    out: RouteRentalTravelStepList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_rental_travel_step.deserialize_json(item)
        )
    return out
