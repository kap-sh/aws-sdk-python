"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanScooterAccessAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_span_scooter_access_attribute

RouteSpanScooterAccessAttributeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_span_scooter_access_attribute.RouteSpanScooterAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanScooterAccessAttributeList) -> list:
    import aws_sdk_geo_routes.types.route_span_scooter_access_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_span_scooter_access_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteSpanScooterAccessAttributeList:
    import aws_sdk_geo_routes.types.route_span_scooter_access_attribute

    out: RouteSpanScooterAccessAttributeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_span_scooter_access_attribute.deserialize_json(
                item
            )
        )
    return out
