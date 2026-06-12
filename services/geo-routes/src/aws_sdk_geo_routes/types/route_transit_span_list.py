"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitSpanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transit_span

RouteTransitSpanList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transit_span.RouteTransitSpan"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitSpanList) -> list:
    import aws_sdk_geo_routes.types.route_transit_span

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_transit_span.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransitSpanList:
    import aws_sdk_geo_routes.types.route_transit_span

    out: RouteTransitSpanList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_transit_span.deserialize_json(item))
    return out
