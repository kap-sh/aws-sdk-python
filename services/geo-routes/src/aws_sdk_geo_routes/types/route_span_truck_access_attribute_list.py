"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanTruckAccessAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_span_truck_access_attribute

RouteSpanTruckAccessAttributeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_span_truck_access_attribute.RouteSpanTruckAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanTruckAccessAttributeList) -> list:
    import aws_sdk_geo_routes.types.route_span_truck_access_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_span_truck_access_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteSpanTruckAccessAttributeList:
    import aws_sdk_geo_routes.types.route_span_truck_access_attribute

    out: RouteSpanTruckAccessAttributeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_span_truck_access_attribute.deserialize_json(
                item
            )
        )
    return out
