"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateVehicleError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.number
    import aws_sdk_iotfleetwise.types.string
    import aws_sdk_iotfleetwise.types.vehicle_name


class UpdateVehicleError(TypedDict, closed=True):
    vehicle_name: NotRequired["aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"]
    """<p>The ID of the vehicle with the error.</p>"""
    code: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The relevant HTTP error code (400+).</p>"""
    message: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>A message associated with the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVehicleError) -> dict:
    out: dict = {}
    if "vehicle_name" in value:
        out["vehicleName"] = value["vehicle_name"]
    out["code"] = value.get("code", 0)
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVehicleError:
    out: UpdateVehicleError = {}  # type: ignore[typeddict-item]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    if "code" in data:
        out["code"] = data["code"]
    else:
        out["code"] = 0
    if "message" in data:
        out["message"] = data["message"]
    return out
