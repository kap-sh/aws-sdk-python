"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.destination_name
    import aws_sdk_iot_wireless.types.fuota_device_status
    import aws_sdk_iot_wireless.types.iso_date_time_string
    import aws_sdk_iot_wireless.types.lo_ra_wan_list_device
    import aws_sdk_iot_wireless.types.mc_group_id
    import aws_sdk_iot_wireless.types.multicast_device_status
    import aws_sdk_iot_wireless.types.positioning_config_status
    import aws_sdk_iot_wireless.types.sidewalk_list_device
    import aws_sdk_iot_wireless.types.wireless_device_arn
    import aws_sdk_iot_wireless.types.wireless_device_id
    import aws_sdk_iot_wireless.types.wireless_device_name
    import aws_sdk_iot_wireless.types.wireless_device_type


class WirelessDeviceStatistics(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_iot_wireless.types.wireless_device_arn.WirelessDeviceArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"]
    """<p>The ID of the wireless device reporting the data.</p>"""
    type: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_type.WirelessDeviceType"
    ]
    """<p>The wireless device type.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_name.WirelessDeviceName"
    ]
    """<p>The name of the resource.</p>"""
    destination_name: NotRequired[
        "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination to which the device is assigned.</p>"""
    last_uplink_received_at: NotRequired[
        "aws_sdk_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the most recent uplink was received.</p> <note> <p>Theis value is only valid for 3 months.</p> </note>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_list_device.LoRaWANListDevice"
    ]
    """<p>LoRaWAN device info.</p>"""
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_list_device.SidewalkListDevice"
    ]
    """<p>The Sidewalk account credentials.</p>"""
    fuota_device_status: NotRequired[
        "aws_sdk_iot_wireless.types.fuota_device_status.FuotaDeviceStatus"
    ]
    multicast_device_status: NotRequired[
        "aws_sdk_iot_wireless.types.multicast_device_status.MulticastDeviceStatus"
    ]
    """<p>The status of the wireless device in the multicast group.</p>"""
    mc_group_id: NotRequired["aws_sdk_iot_wireless.types.mc_group_id.McGroupId"]
    positioning: NotRequired[
        "aws_sdk_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
    ]
    """<p>The integration status of the Device Location feature for LoRaWAN and Amazon Sidewalk enabled devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceStatistics) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import aws_sdk_iot_wireless.types.wireless_device_type

        out["Type"] = aws_sdk_iot_wireless.types.wireless_device_type.serialize_json(
            value["type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "last_uplink_received_at" in value:
        out["LastUplinkReceivedAt"] = value["last_uplink_received_at"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_list_device

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_list_device.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_list_device

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_list_device.serialize_json(
                value["sidewalk"]
            )
        )
    if "fuota_device_status" in value:
        import aws_sdk_iot_wireless.types.fuota_device_status

        out["FuotaDeviceStatus"] = (
            aws_sdk_iot_wireless.types.fuota_device_status.serialize_json(
                value["fuota_device_status"]
            )
        )
    if "multicast_device_status" in value:
        out["MulticastDeviceStatus"] = value["multicast_device_status"]
    if "mc_group_id" in value:
        out["McGroupId"] = value["mc_group_id"]
    if "positioning" in value:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["Positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.serialize_json(
                value["positioning"]
            )
        )
    return out


def deserialize_json(data: dict) -> WirelessDeviceStatistics:
    out: WirelessDeviceStatistics = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_iot_wireless.types.wireless_device_type

        out["type"] = aws_sdk_iot_wireless.types.wireless_device_type.deserialize_json(
            data["Type"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    if "LastUplinkReceivedAt" in data:
        out["last_uplink_received_at"] = data["LastUplinkReceivedAt"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_list_device

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_list_device.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_list_device

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_list_device.deserialize_json(
                data["Sidewalk"]
            )
        )
    if "FuotaDeviceStatus" in data:
        import aws_sdk_iot_wireless.types.fuota_device_status

        out["fuota_device_status"] = (
            aws_sdk_iot_wireless.types.fuota_device_status.deserialize_json(
                data["FuotaDeviceStatus"]
            )
        )
    if "MulticastDeviceStatus" in data:
        out["multicast_device_status"] = data["MulticastDeviceStatus"]
    if "McGroupId" in data:
        out["mc_group_id"] = data["McGroupId"]
    if "Positioning" in data:
        import aws_sdk_iot_wireless.types.positioning_config_status

        out["positioning"] = (
            aws_sdk_iot_wireless.types.positioning_config_status.deserialize_json(
                data["Positioning"]
            )
        )
    return out
