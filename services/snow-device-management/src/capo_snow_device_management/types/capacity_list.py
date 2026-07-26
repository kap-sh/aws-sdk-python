"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snow_device_management.types.capacity

CapacityList: TypeAlias = list["capo_snow_device_management.types.capacity.Capacity"]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityList) -> list:
    import capo_snow_device_management.types.capacity

    out: list = []
    for item in value:
        out.append(capo_snow_device_management.types.capacity.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapacityList:
    import capo_snow_device_management.types.capacity

    out: CapacityList = []
    for item in data:
        out.append(capo_snow_device_management.types.capacity.deserialize_json(item))
    return out
