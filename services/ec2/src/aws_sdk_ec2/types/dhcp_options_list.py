"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_options

DhcpOptionsList: TypeAlias = list["aws_sdk_ec2.types.dhcp_options.DhcpOptions"]
