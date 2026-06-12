"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationDriverOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_rest_cycles
    import aws_sdk_geo_routes.types.waypoint_optimization_rest_profile
    import aws_sdk_geo_routes.types.waypoint_optimization_service_time_treatment


class WaypointOptimizationDriverOptions(TypedDict):
    rest_cycles: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_rest_cycles.WaypointOptimizationRestCycles"
    ]
    """<p>Driver work-rest schedules defined by a short and long cycle. A rest needs to be taken after the short work duration. The short cycle can be repeated until you hit the long work duration, at which point the long rest duration should be taken before restarting.</p>"""
    rest_profile: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_rest_profile.WaypointOptimizationRestProfile"
    ]
    """<p>Pre defined rest profiles for a driver schedule. The only currently supported profile is EU.</p>"""
    treat_service_time_as: NotRequired[
        "aws_sdk_geo_routes.types.waypoint_optimization_service_time_treatment.WaypointOptimizationServiceTimeTreatment"
    ]
    """<p>If the service time provided at a waypoint/destination should be considered as rest or work. This contributes to the total time breakdown returned within the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationDriverOptions) -> dict:
    out: dict = {}
    if "rest_cycles" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_rest_cycles

        out["RestCycles"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_rest_cycles.serialize_json(
                value["rest_cycles"]
            )
        )
    if "rest_profile" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_rest_profile

        out["RestProfile"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_rest_profile.serialize_json(
                value["rest_profile"]
            )
        )
    if "treat_service_time_as" in value:
        import aws_sdk_geo_routes.types.waypoint_optimization_service_time_treatment

        out["TreatServiceTimeAs"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_service_time_treatment.serialize_json(
                value["treat_service_time_as"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationDriverOptions:
    out: WaypointOptimizationDriverOptions = {}  # type: ignore[typeddict-item]
    if "RestCycles" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_rest_cycles

        out["rest_cycles"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_rest_cycles.deserialize_json(
                data["RestCycles"]
            )
        )
    if "RestProfile" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_rest_profile

        out["rest_profile"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_rest_profile.deserialize_json(
                data["RestProfile"]
            )
        )
    if "TreatServiceTimeAs" in data:
        import aws_sdk_geo_routes.types.waypoint_optimization_service_time_treatment

        out["treat_service_time_as"] = (
            aws_sdk_geo_routes.types.waypoint_optimization_service_time_treatment.deserialize_json(
                data["TreatServiceTimeAs"]
            )
        )
    return out
