"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNoticeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_vehicle_notice

RouteVehicleNoticeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_vehicle_notice.RouteVehicleNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNoticeList) -> list:
    import aws_sdk_geo_routes.types.route_vehicle_notice

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_vehicle_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleNoticeList:
    import aws_sdk_geo_routes.types.route_vehicle_notice

    out: RouteVehicleNoticeList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_vehicle_notice.deserialize_json(item))
    return out
