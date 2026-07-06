"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateWirelessDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.lo_ra_wan_update_device
    import aws_sdk_iot_wireless.types.positioning_config_status
    import aws_sdk_iot_wireless.types.sidewalk_update_wireless_device
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_device_name


class UpdateWirelessDeviceRequest(TypedDict, closed=True):
    id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the resource to update.</p>"""
    destination_name: NotRequired[
        "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the new destination for the device.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_name.WirelessDeviceName"
    ]
    """<p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>A new description of the resource.</p>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_update_device.LoRaWANUpdateDevice"
    ]
    """<p>The updated wireless device's configuration.</p>"""
    positioning: NotRequired[
        "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>"""
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_update_wireless_device.SidewalkUpdateWirelessDevice"
    ]
    """<p>The updated sidewalk properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWirelessDeviceRequest) -> dict:
    out: dict = {}
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_update_device

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_update_device.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "positioning" in value:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_update_wireless_device

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_update_wireless_device.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWirelessDeviceRequest:
    out: UpdateWirelessDeviceRequest = {}  # type: ignore[typeddict-item]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_update_device

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_update_device.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Positioning" in data:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_update_wireless_device

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_update_wireless_device.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
