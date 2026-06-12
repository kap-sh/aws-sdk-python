"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateVehicleResponseItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.vehicle_name


class CreateVehicleResponseItem(TypedDict):
    vehicle_name: NotRequired["aws_sdk_iotfleetwise.types.vehicle_name.vehicleName"]
    """<p>The unique ID of the vehicle to create.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the created vehicle.</p>"""
    thing_arn: NotRequired["aws_sdk_iotfleetwise.types.arn.arn"]
    """<p>The ARN of a created or validated Amazon Web Services IoT thing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVehicleResponseItem) -> dict:
    out: dict = {}
    if "vehicle_name" in value:
        out["vehicleName"] = value["vehicle_name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVehicleResponseItem:
    out: CreateVehicleResponseItem = {}  # type: ignore[typeddict-item]
    if "vehicleName" in data:
        out["vehicle_name"] = data["vehicleName"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    return out
