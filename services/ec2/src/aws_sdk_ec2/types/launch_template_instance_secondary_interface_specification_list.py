"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceSecondaryInterfaceSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification

LaunchTemplateInstanceSecondaryInterfaceSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification.LaunchTemplateInstanceSecondaryInterfaceSpecification"
]
