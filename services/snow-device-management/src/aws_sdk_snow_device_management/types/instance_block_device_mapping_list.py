"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#InstanceBlockDeviceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.instance_block_device_mapping

InstanceBlockDeviceMappingList: TypeAlias = list[
    "aws_sdk_snow_device_management.types.instance_block_device_mapping.InstanceBlockDeviceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceBlockDeviceMappingList) -> list:
    import aws_sdk_snow_device_management.types.instance_block_device_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snow_device_management.types.instance_block_device_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstanceBlockDeviceMappingList:
    import aws_sdk_snow_device_management.types.instance_block_device_mapping

    out: InstanceBlockDeviceMappingList = []
    for item in data:
        out.append(
            aws_sdk_snow_device_management.types.instance_block_device_mapping.deserialize_json(
                item
            )
        )
    return out
