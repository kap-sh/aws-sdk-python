"""Generated from Smithy shape ``com.amazonaws.ec2#NewDhcpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.new_dhcp_configuration

NewDhcpConfigurationList: TypeAlias = list[
    "aws_sdk_ec2.types.new_dhcp_configuration.NewDhcpConfiguration"
]
