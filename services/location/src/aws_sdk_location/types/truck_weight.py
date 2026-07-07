"""Generated from Smithy shape ``com.amazonaws.location#TruckWeight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.sensitive_double
    import aws_sdk_location.types.vehicle_weight_unit


class TruckWeight(TypedDict, closed=True):
    total: NotRequired["aws_sdk_location.types.sensitive_double.SensitiveDouble"]
    """<p>The total weight of the truck. </p> <ul> <li> <p>For example, <code>3500</code>.</p> </li> </ul>"""
    unit: NotRequired["aws_sdk_location.types.vehicle_weight_unit.VehicleWeightUnit"]
    """<p>The unit of measurement to use for the truck weight.</p> <p>Default Value: <code>Kilograms</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TruckWeight) -> dict:
    out: dict = {}
    if "total" in value:
        out["Total"] = value["total"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> TruckWeight:
    out: TruckWeight = {}  # type: ignore[typeddict-item]
    if "Total" in data:
        out["total"] = data["Total"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
