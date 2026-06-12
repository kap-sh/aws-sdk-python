"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanPedestrianAccessAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_span_pedestrian_access_attribute

RouteSpanPedestrianAccessAttributeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_span_pedestrian_access_attribute.RouteSpanPedestrianAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanPedestrianAccessAttributeList) -> list:
    import aws_sdk_geo_routes.types.route_span_pedestrian_access_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_span_pedestrian_access_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteSpanPedestrianAccessAttributeList:
    import aws_sdk_geo_routes.types.route_span_pedestrian_access_attribute

    out: RouteSpanPedestrianAccessAttributeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_span_pedestrian_access_attribute.deserialize_json(
                item
            )
        )
    return out
