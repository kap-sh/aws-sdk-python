"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_configuration

DhcpConfigurationList: TypeAlias = list[
    "aws_sdk_ec2.types.dhcp_configuration.DhcpConfiguration"
]
