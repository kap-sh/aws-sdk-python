"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfDevice``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.device

__listOfDevice: TypeAlias = list["capo_greengrass.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDevice) -> list:
    import capo_greengrass.types.device

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDevice:
    import capo_greengrass.types.device

    out: __listOfDevice = []
    for item in data:
        out.append(capo_greengrass.types.device.deserialize_json(item))
    return out
