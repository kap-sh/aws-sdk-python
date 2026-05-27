"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteInstallationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_route_installation_detail

RouteServerRouteInstallationDetails: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_route_installation_detail.RouteServerRouteInstallationDetail"
]
