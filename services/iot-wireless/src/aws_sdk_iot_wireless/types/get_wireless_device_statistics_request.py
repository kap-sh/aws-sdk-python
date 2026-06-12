"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessDeviceStatisticsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_id


class GetWirelessDeviceStatisticsRequest(TypedDict):
    wireless_device_id: "aws_sdk_iot_wireless.types.wireless_device_id.WirelessDeviceId"
    """<p>The ID of the wireless device for which to get the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessDeviceStatisticsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessDeviceStatisticsRequest:
    out: GetWirelessDeviceStatisticsRequest = {}  # type: ignore[typeddict-item]
    return out
