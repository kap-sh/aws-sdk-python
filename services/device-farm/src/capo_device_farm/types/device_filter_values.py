"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.string

DeviceFilterValues: TypeAlias = list["capo_device_farm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeviceFilterValues:
    return list(data)
