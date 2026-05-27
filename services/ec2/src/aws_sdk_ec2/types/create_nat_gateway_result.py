"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNatGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway
    import aws_sdk_ec2.types.string


class CreateNatGatewayResult(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
    nat_gateway: NotRequired["aws_sdk_ec2.types.nat_gateway.NatGateway"]
    """<p>Information about the NAT gateway.</p>"""
