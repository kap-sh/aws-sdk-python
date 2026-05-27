"""Generated from Smithy shape ``com.amazonaws.ec2#VpnStaticRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_static_route

VpnStaticRouteList: TypeAlias = list[
    "aws_sdk_ec2.types.vpn_static_route.VpnStaticRoute"
]
