"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DeleteVehicleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.vehicle_name


class DeleteVehicleRequest(TypedDict, closed=True):
    vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName"
    """<p>The ID of the vehicle to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVehicleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVehicleRequest:
    out: DeleteVehicleRequest = {}  # type: ignore[typeddict-item]
    return out
