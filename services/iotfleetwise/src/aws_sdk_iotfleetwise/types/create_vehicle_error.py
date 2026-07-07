"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateVehicleError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.string
    import aws_sdk_iotfleetwise.types.vehicle_name


class CreateVehicleError(TypedDict, closed=True):
    vehicle_name: NotRequired["aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"]
    """<p>The ID of the vehicle with the error.</p>"""
    code: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>An HTTP error code.</p>"""
    message: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>A description of the HTTP error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVehicleError) -> dict:
    out: dict = {}
    if "vehicle_name" in value:
        out["vehicleName"] = value["vehicle_name"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVehicleError:
    out: CreateVehicleError = {}  # type: ignore[typeddict-item]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
