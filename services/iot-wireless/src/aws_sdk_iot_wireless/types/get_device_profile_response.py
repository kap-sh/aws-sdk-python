"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetDeviceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_profile_arn
    import aws_sdk_iot_wireless.types.device_profile_id
    import aws_sdk_iot_wireless.types.device_profile_name
    import aws_sdk_iot_wireless.types.lo_ra_wan_device_profile
    import aws_sdk_iot_wireless.types.sidewalk_get_device_profile


class GetDeviceProfileResponse(TypedDict):
    arn: NotRequired["aws_sdk_iot_wireless.types.device_profile_arn.DeviceProfileArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.device_profile_name.DeviceProfileName"
    ]
    """<p>The name of the resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"]
    """<p>The ID of the device profile.</p>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_device_profile.LoRaWANDeviceProfile"
    ]
    """<p>Information about the device profile.</p>"""
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_get_device_profile.SidewalkGetDeviceProfile"
    ]
    """<p>Information about the Sidewalk parameters in the device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceProfileResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_device_profile

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_device_profile.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_get_device_profile

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_get_device_profile.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDeviceProfileResponse:
    out: GetDeviceProfileResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_device_profile

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_device_profile.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_get_device_profile

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_get_device_profile.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
