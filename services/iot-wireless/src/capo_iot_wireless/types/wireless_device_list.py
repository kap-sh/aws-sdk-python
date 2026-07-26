"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_device_id

WirelessDeviceList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceList) -> list:
    return list(value)


def deserialize_json(data: list) -> WirelessDeviceList:
    return list(data)
