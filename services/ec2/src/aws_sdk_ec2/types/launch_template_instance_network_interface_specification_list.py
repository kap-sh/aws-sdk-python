"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceNetworkInterfaceSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_instance_network_interface_specification

LaunchTemplateInstanceNetworkInterfaceSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_instance_network_interface_specification.LaunchTemplateInstanceNetworkInterfaceSpecification"
]
