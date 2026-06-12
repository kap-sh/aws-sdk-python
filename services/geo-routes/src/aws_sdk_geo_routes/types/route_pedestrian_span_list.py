"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianSpanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_pedestrian_span

RoutePedestrianSpanList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_pedestrian_span.RoutePedestrianSpan"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianSpanList) -> list:
    import aws_sdk_geo_routes.types.route_pedestrian_span

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_pedestrian_span.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutePedestrianSpanList:
    import aws_sdk_geo_routes.types.route_pedestrian_span

    out: RoutePedestrianSpanList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_pedestrian_span.deserialize_json(item)
        )
    return out
