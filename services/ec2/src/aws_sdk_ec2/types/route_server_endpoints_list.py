"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_endpoint

RouteServerEndpointsList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_endpoint.RouteServerEndpoint"
]
