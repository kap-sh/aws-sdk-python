"""Generated from Smithy shape ``com.amazonaws.panorama#DeviceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_id

DeviceIdList: TypeAlias = list["aws_sdk_panorama.types.device_id.DeviceId"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeviceIdList:
    return list(data)
