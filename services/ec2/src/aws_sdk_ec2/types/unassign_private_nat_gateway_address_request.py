"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignPrivateNatGatewayAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.drain_seconds
    import aws_sdk_ec2.types.ip_list
    import aws_sdk_ec2.types.nat_gateway_id


class UnassignPrivateNatGatewayAddressRequest(TypedDict):
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>The ID of the NAT gateway.</p>"""
    private_ip_addresses: NotRequired["aws_sdk_ec2.types.ip_list.IpList"]
    """<p>The private IPv4 addresses you want to unassign.</p>"""
    max_drain_duration_seconds: NotRequired[
        "aws_sdk_ec2.types.drain_seconds.DrainSeconds"
    ]
    """<p>The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. Default value is 350 seconds.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
