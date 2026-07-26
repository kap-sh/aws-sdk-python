"""Generated from Smithy shape ``com.amazonaws.wickr#Devices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.basic_device_object

Devices: TypeAlias = list["capo_wickr.types.basic_device_object.BasicDeviceObject"]


# --- restJson1 ser/de ---
def serialize_json(value: Devices) -> list:
    import capo_wickr.types.basic_device_object

    out: list = []
    for item in value:
        out.append(capo_wickr.types.basic_device_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> Devices:
    import capo_wickr.types.basic_device_object

    out: Devices = []
    for item in data:
        out.append(capo_wickr.types.basic_device_object.deserialize_json(item))
    return out
