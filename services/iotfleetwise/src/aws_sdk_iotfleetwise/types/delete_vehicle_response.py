"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DeleteVehicleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.vehicle_name


class DeleteVehicleResponse(TypedDict):
    vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"
    """<p>The ID of the deleted vehicle.</p>"""
    arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the deleted vehicle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVehicleResponse) -> dict:
    out: dict = {}
    out["vehicleName"] = value["vehicle_name"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVehicleResponse:
    out: DeleteVehicleResponse = {}  # type: ignore[typeddict-item]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    else:
        raise DeserializationError("DeleteVehicleResponse.vehicle_name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteVehicleResponse.arn required")
    return out
