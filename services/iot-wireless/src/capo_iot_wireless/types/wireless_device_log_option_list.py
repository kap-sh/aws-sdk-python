"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceLogOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_device_log_option

WirelessDeviceLogOptionList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_device_log_option.WirelessDeviceLogOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceLogOptionList) -> list:
    import capo_iot_wireless.types.wireless_device_log_option

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.wireless_device_log_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceLogOptionList:
    import capo_iot_wireless.types.wireless_device_log_option

    out: WirelessDeviceLogOptionList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.wireless_device_log_option.deserialize_json(item)
        )
    return out
