"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationImpedingWaypoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.waypoint_id
    import aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint_list


class WaypointOptimizationImpedingWaypoint(TypedDict, closed=True):
    failed_constraints: "aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint_list.WaypointOptimizationFailedConstraintList"
    """<p>Failed constraints for an impeding waypoint.</p>"""
    id: "aws_sdk_geo_routes.types.waypoint_id.WaypointId"
    """<p>The waypoint Id.</p>"""
    position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationImpedingWaypoint) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint_list

    out["FailedConstraints"] = (
        aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint_list.serialize_json(
            value["failed_constraints"]
        )
    )
    out["Id"] = value["id"]
    import aws_sdk_geo_routes.types.position

    out["Position"] = aws_sdk_geo_routes.types.position.serialize_json(
        value["position"]
    )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationImpedingWaypoint:
    out: WaypointOptimizationImpedingWaypoint = {}  # type: ignore[typeddict-item]
    if "FailedConstraints" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint_list

        out["failed_constraints"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint_list.deserialize_json(
                data["FailedConstraints"]
            )
        )
    else:
        raise DeserializationError(
            "WaypointOptimizationImpedingWaypoint.failed_constraints required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("WaypointOptimizationImpedingWaypoint.id required")
    if "Position" in data:
        import aws_sdk_geo_routes.types.position

        out["position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError(
            "WaypointOptimizationImpedingWaypoint.position required"
        )
    return out
