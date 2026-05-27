"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelOptionsSpecificationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_tunnel_options_specification

VpnTunnelOptionsSpecificationsList: TypeAlias = list[
    "aws_sdk_ec2.types.vpn_tunnel_options_specification.VpnTunnelOptionsSpecification"
]
