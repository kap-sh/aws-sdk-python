"""Generated from Smithy shape ``com.amazonaws.iotwireless#ImportedWirelessDeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.imported_wireless_device

ImportedWirelessDeviceList: TypeAlias = list[
    "capo_iot_wireless.types.imported_wireless_device.ImportedWirelessDevice"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportedWirelessDeviceList) -> list:
    import capo_iot_wireless.types.imported_wireless_device

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.imported_wireless_device.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ImportedWirelessDeviceList:
    import capo_iot_wireless.types.imported_wireless_device

    out: ImportedWirelessDeviceList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.imported_wireless_device.deserialize_json(item)
        )
    return out
