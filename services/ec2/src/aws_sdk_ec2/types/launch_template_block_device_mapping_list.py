"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateBlockDeviceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_block_device_mapping

LaunchTemplateBlockDeviceMappingList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_block_device_mapping.LaunchTemplateBlockDeviceMapping"
]
