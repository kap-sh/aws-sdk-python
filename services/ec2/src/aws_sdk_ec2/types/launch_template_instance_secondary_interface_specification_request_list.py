"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification_request

LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification_request.LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest"
]
