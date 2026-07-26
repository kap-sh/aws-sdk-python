"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessDeviceStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.iso_date_time_string
    import capo_iot_wireless.types.lo_ra_wan_device_metadata
    import capo_iot_wireless.types.sidewalk_device_metadata
    import capo_iot_wireless.types.wireless_device_id


class GetWirelessDeviceStatisticsResponse(TypedDict, closed=True):
    wireless_device_id: NotRequired[
        "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    ]
    """<p>The ID of the wireless device.</p>"""
    last_uplink_received_at: NotRequired[
        "capo_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the most recent uplink was received.</p> <note> <p>This value is only valid for 3 months.</p> </note>"""
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_device_metadata.LoRaWANDeviceMetadata"
    ]
    """<p>Information about the wireless device's operations.</p>"""
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_device_metadata.SidewalkDeviceMetadata"
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
        import capo_iot_wireless.types.lo_ra_wan_device_metadata

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_device_metadata.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_device_metadata

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_device_metadata.serialize_json(
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
        import capo_iot_wireless.types.lo_ra_wan_device_metadata

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_device_metadata.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_device_metadata

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_device_metadata.deserialize_json(
                data["Sidewalk"]
            )
        )
    return out
