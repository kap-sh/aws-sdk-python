"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateNatGatewayAddressResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_address_list
    import aws_sdk_ec2.types.nat_gateway_id


class AssociateNatGatewayAddressResult(TypedDict):
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>The ID of the NAT gateway.</p>"""
    nat_gateway_addresses: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_address_list.NatGatewayAddressList"
    ]
    """<p>The IP addresses.</p>"""
