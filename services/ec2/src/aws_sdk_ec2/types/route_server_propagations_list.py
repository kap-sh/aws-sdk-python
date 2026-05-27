"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPropagationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_propagation

RouteServerPropagationsList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_propagation.RouteServerPropagation"
]
