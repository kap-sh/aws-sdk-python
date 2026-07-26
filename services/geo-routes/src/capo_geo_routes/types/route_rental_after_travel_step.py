"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalAfterTravelStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_rental_after_travel_step_type
    import capo_geo_routes.types.sensitive_string


class RouteRentalAfterTravelStep(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p>"""
    type: "capo_geo_routes.types.route_rental_after_travel_step_type.RouteRentalAfterTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalAfterTravelStep) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import capo_geo_routes.types.route_rental_after_travel_step_type

    out["Type"] = (
        capo_geo_routes.types.route_rental_after_travel_step_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteRentalAfterTravelStep:
    out: RouteRentalAfterTravelStep = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteRentalAfterTravelStep.duration required")
    if "Instruction" in data:
        out["instruction"] = data["Instruction"]
    if "Type" in data:
        import capo_geo_routes.types.route_rental_after_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_rental_after_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteRentalAfterTravelStep.type required")
    return out
