"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleAfterTravelStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_charge_step_details
    import capo_geo_routes.types.route_vehicle_after_travel_step_type
    import capo_geo_routes.types.sensitive_string


class RouteVehicleAfterTravelStep(TypedDict, closed=True):
    charge_step_details: NotRequired[
        "capo_geo_routes.types.route_charge_step_details.RouteChargeStepDetails"
    ]
    """<p>Details that are specific to a Charge step.</p> <p> <b>Unit</b>: <code>KwH </code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p> <note> <p>Only available when the TravelStepType is Default.</p> </note>"""
    type: "capo_geo_routes.types.route_vehicle_after_travel_step_type.RouteVehicleAfterTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleAfterTravelStep) -> dict:
    out: dict = {}
    if "charge_step_details" in value:
        import capo_geo_routes.types.route_charge_step_details

        out["ChargeStepDetails"] = (
            capo_geo_routes.types.route_charge_step_details.serialize_json(
                value["charge_step_details"]
            )
        )
    out["Duration"] = value["duration"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import capo_geo_routes.types.route_vehicle_after_travel_step_type

    out["Type"] = (
        capo_geo_routes.types.route_vehicle_after_travel_step_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteVehicleAfterTravelStep:
    out: RouteVehicleAfterTravelStep = {}  # type: ignore[typeddict-item]
    if "ChargeStepDetails" in data:
        import capo_geo_routes.types.route_charge_step_details

        out["charge_step_details"] = (
            capo_geo_routes.types.route_charge_step_details.deserialize_json(
                data["ChargeStepDetails"]
            )
        )
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteVehicleAfterTravelStep.duration required")
    if "Instruction" in data:
        out["instruction"] = data["Instruction"]
    if "Type" in data:
        import capo_geo_routes.types.route_vehicle_after_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_vehicle_after_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleAfterTravelStep.type required")
    return out
