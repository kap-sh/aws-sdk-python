"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanCarAccessAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_span_car_access_attribute

RouteSpanCarAccessAttributeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_span_car_access_attribute.RouteSpanCarAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanCarAccessAttributeList) -> list:
    import aws_sdk_geo_routes.types.route_span_car_access_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_span_car_access_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteSpanCarAccessAttributeList:
    import aws_sdk_geo_routes.types.route_span_car_access_attribute

    out: RouteSpanCarAccessAttributeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_span_car_access_attribute.deserialize_json(
                item
            )
        )
    return out
