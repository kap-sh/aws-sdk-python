"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#AssociateVehicleFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.fleet_id
    import aws_sdk_iotfleetwise.types.vehicle_name


class AssociateVehicleFleetRequest(TypedDict, closed=True):
    vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"
    """<p> The unique ID of the vehicle to associate with the fleet. </p>"""
    fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of a fleet. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateVehicleFleetRequest) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateVehicleFleetRequest:
    out: AssociateVehicleFleetRequest = {}  # type: ignore[typeddict-item]
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("AssociateVehicleFleetRequest.fleet_id required")
    return out
