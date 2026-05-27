"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_network_interface_specification

InstanceNetworkInterfaceSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_network_interface_specification.InstanceNetworkInterfaceSpecification"
]
