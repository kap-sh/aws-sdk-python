"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_route

RouteServerRouteList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_route.RouteServerRoute"
]
