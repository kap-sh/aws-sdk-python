"""Generated from Smithy shape ``com.amazonaws.ec2#TunnelOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.tunnel_option

TunnelOptionsList: TypeAlias = list["aws_sdk_ec2.types.tunnel_option.TunnelOption"]
