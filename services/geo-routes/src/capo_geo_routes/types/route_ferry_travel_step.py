"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryTravelStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_ferry_travel_step_type
    import capo_geo_routes.types.sensitive_string


class RouteFerryTravelStep(TypedDict, closed=True):
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the step.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p> <note> <p>Only available when the TravelStepType is Default.</p> </note>"""
    type: "capo_geo_routes.types.route_ferry_travel_step_type.RouteFerryTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryTravelStep) -> dict:
    out: dict = {}
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import capo_geo_routes.types.route_ferry_travel_step_type

    out["Type"] = capo_geo_routes.types.route_ferry_travel_step_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> RouteFerryTravelStep:
    out: RouteFerryTravelStep = {}  # type: ignore[typeddict-item]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    if "Instruction" in data:
        out["instruction"] = data["Instruction"]
    if "Type" in data:
        import capo_geo_routes.types.route_ferry_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_ferry_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteFerryTravelStep.type required")
    return out
