"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetVehicleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.vehicle_name


class GetVehicleRequest(TypedDict):
    vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"
    """<p> The ID of the vehicle to retrieve information about. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVehicleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVehicleRequest:
    out: GetVehicleRequest = {}  # type: ignore[typeddict-item]
    return out
