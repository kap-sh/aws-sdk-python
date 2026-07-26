"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceEventLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_device_event_log_option

WirelessDeviceEventLogOptionList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_device_event_log_option.WirelessDeviceEventLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceEventLogOptionList) -> list:
    import capo_iot_wireless.types.wireless_device_event_log_option

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.wireless_device_event_log_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceEventLogOptionList:
    import capo_iot_wireless.types.wireless_device_event_log_option

    out: WirelessDeviceEventLogOptionList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.wireless_device_event_log_option.deserialize_json(
                item
            )
        )
    return out
