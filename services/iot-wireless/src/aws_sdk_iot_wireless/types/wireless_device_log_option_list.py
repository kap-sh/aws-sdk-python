"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_log_option

WirelessDeviceLogOptionList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.wireless_device_log_option.WirelessDeviceLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceLogOptionList) -> list:
    import aws_sdk_iot_wireless.types.wireless_device_log_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_log_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceLogOptionList:
    import aws_sdk_iot_wireless.types.wireless_device_log_option

    out: WirelessDeviceLogOptionList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_log_option.deserialize_json(item)
        )
    return out
