"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessDeviceStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.iso_date_time_string
    import aws_sdk_iot_wireless.types.lo_ra_wan_device_metadata
    import aws_sdk_iot_wireless.types.sidewalk_device_metadata
    import aws_sdk_iot_wireless.types.wireless_device_id


class GetWirelessDeviceStatisticsResponse(TypedDict):
    wireless_device_id: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    ]
    """<p>The ID of the wireless device.</p>"""
    last_uplink_received_at: NotRequired[
        "aws_sdk_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the most recent uplink was received.</p> <note> <p>This value is only valid for 3 months.</p> </note>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_device_metadata.LoRaWANDeviceMetadata"
    ]
    """<p>Information about the wireless device's operations.</p>"""
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_device_metadata.SidewalkDeviceMetadata"
    ]
    """<p>MetaData for Sidewalk device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessDeviceStatisticsResponse) -> dict:
    out: dict = {}
    if "wireless_device_id" in value:
        out["WirelessDeviceId"] = value["wireless_device_id"]
    if "last_uplink_received_at" in value:
        out["LastUplinkReceivedAt"] = value["last_uplink_received_at"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_device_metadata

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_device_metadata.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_device_metadata

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_device_metadata.serialize_json(
                value["sidewalk"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWirelessDeviceStatisticsResponse:
    out: GetWirelessDeviceStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "WirelessDeviceId" in data:
        out["wireless_device_id"] = data["WirelessDeviceId"]
    if "LastUplinkReceivedAt" in data:
        out["last_uplink_received_at"] = data["LastUplinkReceivedAt"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_device_metadata

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_device_metadata.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_device_metadata

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_device_metadata.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
