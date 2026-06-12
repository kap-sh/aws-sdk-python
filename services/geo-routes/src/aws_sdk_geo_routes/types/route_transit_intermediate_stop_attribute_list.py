"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStopAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute

RouteTransitIntermediateStopAttributeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute.RouteTransitIntermediateStopAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIntermediateStopAttributeList) -> list:
    import aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteTransitIntermediateStopAttributeList:
    import aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute

    out: RouteTransitIntermediateStopAttributeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_transit_intermediate_stop_attribute.deserialize_json(
                item
            )
        )
    return out
