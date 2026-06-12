"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InstanceBlockDeviceMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.instance_block_device_mapping

InstanceBlockDeviceMappings: TypeAlias = list[
    "aws_sdk_imagebuilder.types.instance_block_device_mapping.InstanceBlockDeviceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceBlockDeviceMappings) -> list:
    import aws_sdk_imagebuilder.types.instance_block_device_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.instance_block_device_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstanceBlockDeviceMappings:
    import aws_sdk_imagebuilder.types.instance_block_device_mapping

    out: InstanceBlockDeviceMappings = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.instance_block_device_mapping.deserialize_json(
                item
            )
        )
    return out
