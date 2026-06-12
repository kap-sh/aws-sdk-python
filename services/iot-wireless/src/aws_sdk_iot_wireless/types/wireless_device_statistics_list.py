"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceStatisticsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_statistics

WirelessDeviceStatisticsList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.wireless_device_statistics.WirelessDeviceStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceStatisticsList) -> list:
    import aws_sdk_iot_wireless.types.wireless_device_statistics

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_statistics.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceStatisticsList:
    import aws_sdk_iot_wireless.types.wireless_device_statistics

    out: WirelessDeviceStatisticsList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_statistics.deserialize_json(item)
        )
    return out
