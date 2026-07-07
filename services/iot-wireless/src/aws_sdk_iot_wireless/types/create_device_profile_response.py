"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateDeviceProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_profile_arn
    import aws_sdk_iot_wireless.types.device_profile_id


class CreateDeviceProfileResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_iot_wireless.types.device_profile_arn.DeviceProfileArn"]
    """<p>The Amazon Resource Name of the new resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"]
    """<p>The ID of the new device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeviceProfileResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateDeviceProfileResponse:
    out: CreateDeviceProfileResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
