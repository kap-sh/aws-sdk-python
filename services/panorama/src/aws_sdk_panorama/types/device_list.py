"""Generated from Smithy shape ``com.amazonaws.panorama#DeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device

DeviceList: TypeAlias = list["aws_sdk_panorama.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceList) -> list:
    import aws_sdk_panorama.types.device

    out: list = []
    for item in value:
        out.append(aws_sdk_panorama.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceList:
    import aws_sdk_panorama.types.device

    out: DeviceList = []
    for item in data:
        out.append(aws_sdk_panorama.types.device.deserialize_json(item))
    return out
