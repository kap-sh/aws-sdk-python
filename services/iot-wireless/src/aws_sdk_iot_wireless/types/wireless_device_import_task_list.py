"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceImportTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_device_import_task

WirelessDeviceImportTaskList: TypeAlias = list[
    "aws_sdk_iot_wireless.types.wireless_device_import_task.WirelessDeviceImportTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceImportTaskList) -> list:
    import aws_sdk_iot_wireless.types.wireless_device_import_task

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_import_task.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WirelessDeviceImportTaskList:
    import aws_sdk_iot_wireless.types.wireless_device_import_task

    out: WirelessDeviceImportTaskList = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.wireless_device_import_task.deserialize_json(
                item
            )
        )
    return out
