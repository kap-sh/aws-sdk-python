"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateVehicleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.vehicle_name


class UpdateVehicleResponse(TypedDict, closed=True):
    vehicle_name: NotRequired["capo_iotfleetwise.types.vehicle_name.vehicleName"]
    """<p>The ID of the updated vehicle.</p>"""
    arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the updated vehicle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVehicleResponse) -> dict:
    out: dict = {}
    if "vehicle_name" in value:
        out["vehicleName"] = value["vehicle_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVehicleResponse:
    out: UpdateVehicleResponse = {}  # type: ignore[typeddict-item]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
