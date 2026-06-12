"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.lo_ra_wan_device
    import aws_sdk_iot_wireless.types.positioning_config_status
    import aws_sdk_iot_wireless.types.sidewalk_device
    import aws_sdk_iot_wireless.types.thing_arn
    import aws_sdk_iot_wireless.types.thing_name
    import aws_sdk_iot_wireless.types.wireless_device_arn
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_device_name
    import aws_sdk_iot_wireless.types.wireless_device_type


class GetWirelessDeviceResponse(TypedDict):
    type: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>The wireless device type.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_name.WirelessDeviceName"
    ]
    """<p>The name of the resource.</p>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>The description of the resource.</p>"""
    destination_name: NotRequired[
        "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination to which the device is assigned.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"]
    """<p>The ID of the wireless device.</p>"""
    arn: NotRequired["aws_sdk_iot_wireless.types.wireless_device_arn.WirelessDeviceArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    thing_name: NotRequired["aws_sdk_iot_wireless.types.thing_name.ThingName"]
    """<p>The name of the thing associated with the wireless device. The value is empty if a thing isn't associated with the device.</p>"""
    thing_arn: NotRequired["aws_sdk_iot_wireless.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing associated with the wireless device.</p>"""
    lo_ra_wan: NotRequired["aws_sdk_iot_wireless.types.lo_ra_wan_device.LoRaWANDevice"]
    """<p>Information about the wireless device.</p>"""
    sidewalk: NotRequired["aws_sdk_iot_wireless.types.sidewalk_device.SidewalkDevice"]
    """<p>Sidewalk device object.</p>"""
    positioning: NotRequired[
        "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessDeviceResponse) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_iot_wireless.types.wireless_device_type

        out["Type"] = aws_sdk_iot_wireless.types.wireless_device_type.serialize_json(
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
        import aws_sdk_iot_wireless.types.lo_ra_wan_device

        out["LoRaWAN"] = aws_sdk_iot_wireless.types.lo_ra_wan_device.serialize_json(
            value["lo_ra_wan"]
        )
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_device

        out["Sidewalk"] = aws_sdk_iot_wireless.types.sidewalk_device.serialize_json(
            value["sidewalk"]
        )
    if "positioning" in value:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWirelessDeviceResponse:
    out: GetWirelessDeviceResponse = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_iot_wireless.types.wireless_device_type

        out["type"] = aws_sdk_iot_wireless.types.wireless_device_type.deserialize_json(
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
        import aws_sdk_iot_wireless.types.lo_ra_wan_device

        out["lo_ra_wan"] = aws_sdk_iot_wireless.types.lo_ra_wan_device.deserialize_json(
            data["LoRaWAN"]
        )
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_device

        out["sidewalk"] = aws_sdk_iot_wireless.types.sidewalk_device.deserialize_json(
            data["Sidewalk"]
        )
    if "Positioning" in data:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    return out
