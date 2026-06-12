"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationConnection``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.waypoint_id

WaypointOptimizationConnection = TypedDict(
    "WaypointOptimizationConnection",
    {
        "distance": "aws_sdk_geo_routes.types.distance_meters.DistanceMeters",
        "from": "aws_sdk_geo_routes.types.waypoint_id.WaypointId",
        "rest_duration": "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds",
        "to": "aws_sdk_geo_routes.types.waypoint_id.WaypointId",
        "travel_duration": "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds",
        "wait_duration": "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds",
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationConnection) -> dict:
    out: dict = {}
    out["Distance"] = value.get("distance", 0)
    out["From"] = value["from"]
    out["RestDuration"] = value.get("rest_duration", 0)
    out["To"] = value["to"]
    out["TravelDuration"] = value.get("travel_duration", 0)
    out["WaitDuration"] = value.get("wait_duration", 0)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationConnection:
    out: WaypointOptimizationConnection = {}  # type: ignore[typeddict-item]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "From" in data:
        out["from"] = data["From"]
    else:
        raise DeserializationError("WaypointOptimizationConnection.from required")
    if "RestDuration" in data:
        out["rest_duration"] = data["RestDuration"]
    else:
        out["rest_duration"] = 0
    if "To" in data:
        out["to"] = data["To"]
    else:
        raise DeserializationError("WaypointOptimizationConnection.to required")
    if "TravelDuration" in data:
        out["travel_duration"] = data["TravelDuration"]
    else:
        out["travel_duration"] = 0
    if "WaitDuration" in data:
        out["wait_duration"] = data["WaitDuration"]
    else:
        out["wait_duration"] = 0
    return out
