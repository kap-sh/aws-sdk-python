"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleSpanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_vehicle_span

RouteVehicleSpanList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_vehicle_span.RouteVehicleSpan"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleSpanList) -> list:
    import aws_sdk_geo_routes.types.route_vehicle_span

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_vehicle_span.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleSpanList:
    import aws_sdk_geo_routes.types.route_vehicle_span

    out: RouteVehicleSpanList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_vehicle_span.deserialize_json(item))
    return out
