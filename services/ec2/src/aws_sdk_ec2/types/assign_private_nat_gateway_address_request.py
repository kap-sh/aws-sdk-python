"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateNatGatewayAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ip_list
    import aws_sdk_ec2.types.nat_gateway_id
    import aws_sdk_ec2.types.private_ip_address_count


class AssignPrivateNatGatewayAddressRequest(TypedDict):
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>The ID of the NAT gateway.</p>"""
    private_ip_addresses: NotRequired["aws_sdk_ec2.types.ip_list.IpList"]
    """<p>The private IPv4 addresses you want to assign to the private NAT gateway.</p>"""
    private_ip_address_count: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_count.PrivateIpAddressCount"
    ]
    """<p>The number of private IP addresses to assign to the NAT gateway. You can't specify this parameter when also specifying private IP addresses.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
