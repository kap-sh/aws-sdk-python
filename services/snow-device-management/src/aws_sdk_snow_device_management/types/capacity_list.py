"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#CapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.capacity

CapacityList: TypeAlias = list["aws_sdk_snow_device_management.types.capacity.Capacity"]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityList) -> list:
    import aws_sdk_snow_device_management.types.capacity

    out: list = []
    for item in value:
        out.append(aws_sdk_snow_device_management.types.capacity.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapacityList:
    import aws_sdk_snow_device_management.types.capacity

    out: CapacityList = []
    for item in data:
        out.append(aws_sdk_snow_device_management.types.capacity.deserialize_json(item))
    return out
