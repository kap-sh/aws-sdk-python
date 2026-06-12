"""Generated from Smithy shape ``com.amazonaws.location#DevicePositionList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.device_position

DevicePositionList: TypeAlias = list["aws_sdk_location.types.device_position.DevicePosition"]


# --- restJson1 ser/de ---
def serialize_json(value: DevicePositionList) -> list:
    import aws_sdk_location.types.device_position
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.device_position.serialize_json(item))
    return out


def deserialize_json(data: list) -> DevicePositionList:
    import aws_sdk_location.types.device_position
    out: DevicePositionList = []
    for item in data:
        out.append(aws_sdk_location.types.device_position.deserialize_json(item))
    return out