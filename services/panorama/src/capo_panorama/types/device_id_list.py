"""Generated from Smithy shape ``com.amazonaws.panorama#DeviceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.device_id

DeviceIdList: TypeAlias = list["capo_panorama.types.device_id.DeviceId"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeviceIdList:
    return list(data)
