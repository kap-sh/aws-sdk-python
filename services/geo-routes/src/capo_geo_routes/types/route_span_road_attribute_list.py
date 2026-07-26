"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanRoadAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_span_road_attribute

RouteSpanRoadAttributeList: TypeAlias = list[
    "capo_geo_routes.types.route_span_road_attribute.RouteSpanRoadAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanRoadAttributeList) -> list:
    import capo_geo_routes.types.route_span_road_attribute

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_span_road_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteSpanRoadAttributeList:
    import capo_geo_routes.types.route_span_road_attribute

    out: RouteSpanRoadAttributeList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_span_road_attribute.deserialize_json(item)
        )
    return out
