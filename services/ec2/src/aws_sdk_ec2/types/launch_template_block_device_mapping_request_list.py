"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateBlockDeviceMappingRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_block_device_mapping_request

LaunchTemplateBlockDeviceMappingRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_block_device_mapping_request.LaunchTemplateBlockDeviceMappingRequest"
]
