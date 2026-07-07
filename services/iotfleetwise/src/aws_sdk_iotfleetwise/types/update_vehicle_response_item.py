"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateVehicleResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.vehicle_name


class UpdateVehicleResponseItem(TypedDict, closed=True):
    vehicle_name: NotRequired["aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"]
    """<p>The unique ID of the updated vehicle.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the updated vehicle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVehicleResponseItem) -> dict:
    out: dict = {}
    if "vehicle_name" in value:
        out["vehicleName"] = value["vehicle_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVehicleResponseItem:
    out: UpdateVehicleResponseItem = {}  # type: ignore[typeddict-item]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
