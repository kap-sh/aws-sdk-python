"""Generated from Smithy shape ``com.amazonaws.location#DevicePositionUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.device_position_update

DevicePositionUpdateList: TypeAlias = list[
    "aws_sdk_location.types.device_position_update.DevicePositionUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: DevicePositionUpdateList) -> list:
    import aws_sdk_location.types.device_position_update

    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.device_position_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> DevicePositionUpdateList:
    import aws_sdk_location.types.device_position_update

    out: DevicePositionUpdateList = []
    for item in data:
        out.append(aws_sdk_location.types.device_position_update.deserialize_json(item))
    return out
