"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceEventLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_event_log_option

WirelessDeviceEventLogOptionList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.wireless_device_event_log_option.WirelessDeviceEventLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceEventLogOptionList) -> list:
    import aws_sdk_iot_wireless.types.wireless_device_event_log_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_event_log_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceEventLogOptionList:
    import aws_sdk_iot_wireless.types.wireless_device_event_log_option

    out: WirelessDeviceEventLogOptionList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_event_log_option.deserialize_json(
                item
            )
        )
    return out
