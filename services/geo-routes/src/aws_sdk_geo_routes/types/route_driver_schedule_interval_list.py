"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDriverScheduleIntervalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_driver_schedule_interval

RouteDriverScheduleIntervalList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_driver_schedule_interval.RouteDriverScheduleInterval"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteDriverScheduleIntervalList) -> list:
    import aws_sdk_geo_routes.types.route_driver_schedule_interval

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_driver_schedule_interval.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteDriverScheduleIntervalList:
    import aws_sdk_geo_routes.types.route_driver_schedule_interval

    out: RouteDriverScheduleIntervalList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_driver_schedule_interval.deserialize_json(
                item
            )
        )
    return out
