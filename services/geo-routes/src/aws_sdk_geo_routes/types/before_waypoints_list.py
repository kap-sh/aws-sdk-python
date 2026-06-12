"""Generated from Smithy shape ``com.amazonaws.georoutes#BeforeWaypointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_index

BeforeWaypointsList: TypeAlias = list[
    "aws_sdk_geo_routes.types.waypoint_index.WaypointIndex"
]


# --- restJson1 ser/de ---
def serialize_json(value: BeforeWaypointsList) -> list:
    return list(value)


def deserialize_json(data: list) -> BeforeWaypointsList:
    return list(data)
