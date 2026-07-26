"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_device_statistics

WirelessDeviceStatisticsList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_device_statistics.WirelessDeviceStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceStatisticsList) -> list:
    import capo_iot_wireless.types.wireless_device_statistics

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.wireless_device_statistics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceStatisticsList:
    import capo_iot_wireless.types.wireless_device_statistics

    out: WirelessDeviceStatisticsList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.wireless_device_statistics.deserialize_json(item)
        )
    return out
