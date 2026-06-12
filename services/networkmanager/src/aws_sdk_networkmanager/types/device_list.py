"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.device

DeviceList: TypeAlias = list["aws_sdk_networkmanager.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceList) -> list:
    import aws_sdk_networkmanager.types.device

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceList:
    import aws_sdk_networkmanager.types.device

    out: DeviceList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.device.deserialize_json(item))
    return out
