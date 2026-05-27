"""Generated from Smithy shape ``com.amazonaws.ec2#EndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint

EndpointSet: TypeAlias = list["aws_sdk_ec2.types.client_vpn_endpoint.ClientVpnEndpoint"]
