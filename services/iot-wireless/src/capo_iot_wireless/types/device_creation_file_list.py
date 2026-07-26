"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceCreationFileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.device_creation_file

DeviceCreationFileList: TypeAlias = list[
    "capo_iot_wireless.types.device_creation_file.DeviceCreationFile"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceCreationFileList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeviceCreationFileList:
    return list(data)
