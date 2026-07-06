"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationDrivingDistanceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_driving_distance


class WaypointOptimizationDrivingDistanceOptions(TypedDict, closed=True):
    driving_distance: "aws_sdk_geo_routes.types.waypoint_optimization_driving_distance.WaypointOptimizationDrivingDistance"
    """<p>DrivingDistance assigns all the waypoints that are within driving distance of each other into a single cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationDrivingDistanceOptions) -> dict:
    out: dict = {}
    out["DrivingDistance"] = value.get("driving_distance", 5)
    return out


def deserialize_json(data: dict) -> WaypointOptimizationDrivingDistanceOptions:
    out: WaypointOptimizationDrivingDistanceOptions = {}  # type: ignore[typeddict-item]
    if "DrivingDistance" in data:
        out["driving_distance"] = data["DrivingDistance"]
    else:
        out["driving_distance"] = 5
    return out
