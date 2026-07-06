"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationFailedConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_string
    import aws_sdk_geo_routes.types.waypoint_optimization_constraint


class WaypointOptimizationFailedConstraint(TypedDict, closed=True):
    constraint: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_constraint.WaypointOptimizationConstraint"
    ]
    """<p>The failed constraint.</p>"""
    reason: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Reason for the failed constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationFailedConstraint) -> dict:
    out: dict = {}
    if "constraint" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_constraint

        out["Constraint"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_constraint.serialize_json(
                value["constraint"]
            )
        )
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> WaypointOptimizationFailedConstraint:
    out: WaypointOptimizationFailedConstraint = {}  # type: ignore[typeddict-item]
    if "Constraint" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_constraint

        out["constraint"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_constraint.deserialize_json(
                data["Constraint"]
            )
        )
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
