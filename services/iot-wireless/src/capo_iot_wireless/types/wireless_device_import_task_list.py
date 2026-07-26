"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceImportTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.wireless_device_import_task

WirelessDeviceImportTaskList: TypeAlias = list[
    "capo_iot_wireless.types.wireless_device_import_task.WirelessDeviceImportTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceImportTaskList) -> list:
    import capo_iot_wireless.types.wireless_device_import_task

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.wireless_device_import_task.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceImportTaskList:
    import capo_iot_wireless.types.wireless_device_import_task

    out: WirelessDeviceImportTaskList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.wireless_device_import_task.deserialize_json(item)
        )
    return out
