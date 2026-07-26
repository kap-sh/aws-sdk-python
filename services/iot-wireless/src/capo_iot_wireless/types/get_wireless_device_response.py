"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.lo_ra_wan_device
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.sidewalk_device
    import capo_iot_wireless.types.thing_arn
    import capo_iot_wireless.types.thing_name
    import capo_iot_wireless.types.wireless_device_arn
    import capo_iot_wireless.types.wireless_device_id
    import capo_iot_wireless.types.wireless_device_name
    import capo_iot_wireless.types.wireless_device_type


class GetWirelessDeviceResponse(TypedDict, closed=True):
    type: NotRequired["capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"]
    """<p>The wireless device type.</p>"""
    name: NotRequired["capo_iot_wireless.types.wireless_device_name.WirelessDeviceName"]
    """<p>The name of the resource.</p>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>The description of the resource.</p>"""
    destination_name: NotRequired[
        "capo_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination to which the device is assigned.</p>"""
    id: NotRequired["capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"]
    """<p>The ID of the wireless device.</p>"""
    arn: NotRequired["capo_iot_wireless.types.wireless_device_arn.WirelessDeviceArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    thing_name: NotRequired["capo_iot_wireless.types.thing_name.ThingName"]
    """<p>The name of the thing associated with the wireless device. The value is empty if a thing isn't associated with the device.</p>"""
    thing_arn: NotRequired["capo_iot_wireless.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing associated with the wireless device.</p>"""
    lo_ra_wan: NotRequired["capo_iot_wireless.types.lo_ra_wan_device.LoRaWANDevice"]
    """<p>Information about the wireless device.</p>"""
    sidewalk: NotRequired["capo_iot_wireless.types.sidewalk_device.SidewalkDevice"]
    """<p>Sidewalk device object.</p>"""
    positioning: NotRequired[
        "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessDeviceResponse) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_iot_wireless.types.wireless_device_type

        out["Type"] = capo_iot_wireless.types.wireless_device_type.serialize_json(
            value["type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "thing_name" in value:
        out["ThingName"] = value["thing_name"]
    if "thing_arn" in value:
        out["ThingArn"] = value["thing_arn"]
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_device

        out["LoRaWAN"] = capo_iot_wireless.types.lo_ra_wan_device.serialize_json(
            value["lo_ra_wan"]
        )
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_device

        out["Sidewalk"] = capo_iot_wireless.types.sidewalk_device.serialize_json(
            value["sidewalk"]
        )
    if "positioning" in value:
        import capo_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            capo_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWirelessDeviceResponse:
    out: GetWirelessDeviceResponse = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_iot_wireless.types.wireless_device_type

        out["type"] = capo_iot_wireless.types.wireless_device_type.deserialize_json(
            data["Type"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ThingName" in data:
        out["thing_name"] = data["ThingName"]
    if "ThingArn" in data:
        out["thing_arn"] = data["ThingArn"]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_device

        out["lo_ra_wan"] = capo_iot_wireless.types.lo_ra_wan_device.deserialize_json(
            data["LoRaWAN"]
        )
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_device

        out["sidewalk"] = capo_iot_wireless.types.sidewalk_device.deserialize_json(
            data["Sidewalk"]
        )
    if "Positioning" in data:
        import capo_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            capo_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    return out
