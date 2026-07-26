"""Generated from Smithy shape ``com.amazonaws.panorama#DeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.device

DeviceList: TypeAlias = list["capo_panorama.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceList) -> list:
    import capo_panorama.types.device

    out: list = []
    for item in value:
        out.append(capo_panorama.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceList:
    import capo_panorama.types.device

    out: DeviceList = []
    for item in data:
        out.append(capo_panorama.types.device.deserialize_json(item))
    return out
