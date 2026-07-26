"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanPedestrianAccessAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_span_pedestrian_access_attribute

RouteSpanPedestrianAccessAttributeList: TypeAlias = list[
    "capo_geo_routes.types.route_span_pedestrian_access_attribute.RouteSpanPedestrianAccessAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanPedestrianAccessAttributeList) -> list:
    import capo_geo_routes.types.route_span_pedestrian_access_attribute

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_span_pedestrian_access_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteSpanPedestrianAccessAttributeList:
    import capo_geo_routes.types.route_span_pedestrian_access_attribute

    out: RouteSpanPedestrianAccessAttributeList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_span_pedestrian_access_attribute.deserialize_json(
                item
            )
        )
    return out
