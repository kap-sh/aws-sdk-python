"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_profile_arn
    import aws_sdk_iot_wireless.types.device_profile_id
    import aws_sdk_iot_wireless.types.device_profile_name


class DeviceProfile(TypedDict):
    arn: NotRequired["aws_sdk_iot_wireless.types.device_profile_arn.DeviceProfileArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.device_profile_name.DeviceProfileName"
    ]
    """<p>The name of the resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"]
    """<p>The ID of the device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeviceProfile:
    out: DeviceProfile = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
