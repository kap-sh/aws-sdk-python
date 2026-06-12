"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryBeforeTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_ferry_before_travel_step

RouteFerryBeforeTravelStepList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_ferry_before_travel_step.RouteFerryBeforeTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryBeforeTravelStepList) -> list:
    import aws_sdk_geo_routes.types.route_ferry_before_travel_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_ferry_before_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteFerryBeforeTravelStepList:
    import aws_sdk_geo_routes.types.route_ferry_before_travel_step

    out: RouteFerryBeforeTravelStepList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_ferry_before_travel_step.deserialize_json(
                item
            )
        )
    return out
