"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNatGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeleteNatGatewayResult(TypedDict):
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the NAT gateway.</p>"""
