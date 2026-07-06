"""Generated from Smithy shape ``com.amazonaws.georoutes#OptimizeWaypointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.waypoint_optimization_connection_list
    import aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint_list
    import aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint_list
    import aws_sdk_geo_routes.types.waypoint_optimization_time_breakdown


class OptimizeWaypointsResponse(TypedDict, closed=True):
    connections: "aws_sdk_geo_routes.types.waypoint_optimization_connection_list.WaypointOptimizationConnectionList"
    """<p>Details about the connection from one waypoint to the next, within the optimized sequence.</p>"""
    distance: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Overall distance to travel the whole sequence.</p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Overall duration to travel the whole sequence.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    impeding_waypoints: "aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint_list.WaypointOptimizationImpedingWaypointList"
    """<p>Returns waypoints that caused the optimization problem to fail, and the constraints that were unsatisfied leading to the failure.</p>"""
    optimized_waypoints: "aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint_list.WaypointOptimizationOptimizedWaypointList"
    """<p>Waypoints in the order of the optimized sequence.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p>"""
    time_breakdown: "aws_sdk_geo_routes.types.waypoint_optimization_time_breakdown.WaypointOptimizationTimeBreakdown"
    """<p>Time breakdown for the sequence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizeWaypointsResponse) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.waypoint_optimization_connection_list

    out["Connections"] = (
        aws_sdk_geo_routes.types.waypoint_optimization_connection_list.serialize_json(
            value["connections"]
        )
    )
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    import aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint_list

    out["ImpedingWaypoints"] = (
        aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint_list.serialize_json(
            value["impeding_waypoints"]
        )
    )
    import aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint_list

    out["OptimizedWaypoints"] = (
        aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint_list.serialize_json(
            value["optimized_waypoints"]
        )
    )
    import aws_sdk_geo_routes.types.waypoint_optimization_time_breakdown

    out["TimeBreakdown"] = (
        aws_sdk_geo_routes.types.waypoint_optimization_time_breakdown.serialize_json(
            value["time_breakdown"]
        )
    )
    return out


def deserialize_json(data: dict) -> OptimizeWaypointsResponse:
    out: OptimizeWaypointsResponse = {}  # type: ignore[typeddict-item]
    if "Connections" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_connection_list

        out["connections"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_connection_list.deserialize_json(
                data["Connections"]
            )
        )
    else:
        raise DeserializationError("OptimizeWaypointsResponse.connections required")
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "ImpedingWaypoints" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint_list

        out["impeding_waypoints"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint_list.deserialize_json(
                data["ImpedingWaypoints"]
            )
        )
    else:
        raise DeserializationError(
            "OptimizeWaypointsResponse.impeding_waypoints required"
        )
    if "OptimizedWaypoints" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint_list

        out["optimized_waypoints"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint_list.deserialize_json(
                data["OptimizedWaypoints"]
            )
        )
    else:
        raise DeserializationError(
            "OptimizeWaypointsResponse.optimized_waypoints required"
        )
    if "TimeBreakdown" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_time_breakdown

        out["time_breakdown"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_time_breakdown.deserialize_json(
                data["TimeBreakdown"]
            )
        )
    else:
        raise DeserializationError("OptimizeWaypointsResponse.time_breakdown required")
    return out
