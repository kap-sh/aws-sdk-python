"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteChargeStepDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.energy_kilowatt_hours
    import aws_sdk_geo_routes.types.power_kilowatts


class RouteChargeStepDetails(TypedDict):
    arrival_charge: NotRequired[
        "aws_sdk_geo_routes.types.energy_kilowatt_hours.EnergyKilowattHours"
    ]
    """<p>Estimated vehicle battery charge before this step (in kWh). </p>"""
    consumable_power: NotRequired[
        "aws_sdk_geo_routes.types.power_kilowatts.PowerKilowatts"
    ]
    """<p>Maximum charging power available to the vehicle.</p> <p> <b>Unit</b>: <code>KwH</code> </p>"""
    desired_charge: NotRequired[
        "aws_sdk_geo_routes.types.energy_kilowatt_hours.EnergyKilowattHours"
    ]
    """<p>Details that are specific to a Charge step.</p> <p> <b>Unit</b>: <code>KwH</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteChargeStepDetails) -> dict:
    out: dict = {}
    if "arrival_charge" in value:
        out["ArrivalCharge"] = value["arrival_charge"]
    if "consumable_power" in value:
        out["ConsumablePower"] = value["consumable_power"]
    if "desired_charge" in value:
        out["DesiredCharge"] = value["desired_charge"]
    return out


def deserialize_json(data: dict) -> RouteChargeStepDetails:
    out: RouteChargeStepDetails = {}  # type: ignore[typeddict-item]
    if "ArrivalCharge" in data:
        out["arrival_charge"] = data["ArrivalCharge"]
    if "ConsumablePower" in data:
        out["consumable_power"] = data["ConsumablePower"]
    if "DesiredCharge" in data:
        out["desired_charge"] = data["DesiredCharge"]
    return out
