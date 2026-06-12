"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAccessHours``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry

WaypointOptimizationAccessHours = TypedDict(
    "WaypointOptimizationAccessHours",
    {
        "from": "aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry.WaypointOptimizationAccessHoursEntry",
        "to": "aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry.WaypointOptimizationAccessHoursEntry",
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAccessHours) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry

    out["From"] = (
        aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry.serialize_json(
            value["from"]
        )
    )
    import aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry

    out["To"] = (
        aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry.serialize_json(
            value["to"]
        )
    )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationAccessHours:
    out: WaypointOptimizationAccessHours = {}  # type: ignore[typeddict-item]
    if "From" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry

        out["from"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry.deserialize_json(
                data["From"]
            )
        )
    else:
        raise DeserializationError("WaypointOptimizationAccessHours.from required")
    if "To" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry

        out["to"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_access_hours_entry.deserialize_json(
                data["To"]
            )
        )
    else:
        raise DeserializationError("WaypointOptimizationAccessHours.to required")
    return out
