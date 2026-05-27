"""Generated from Smithy shape ``com.amazonaws.ec2#CreateClientVpnRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class CreateClientVpnRouteRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint to which to add the route.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the route destination. For example:</p> <ul> <li> <p>To add a route for Internet access, enter <code>0.0.0.0/0</code> </p> </li> <li> <p>To add a route for a peered VPC, enter the peered VPC's IPv4 CIDR range</p> </li> <li> <p>To add a route for an on-premises network, enter the Amazon Web Services Site-to-Site VPN connection's IPv4 CIDR range</p> </li> <li> <p>To add a route for the local network, enter the client CIDR range</p> </li> </ul>"""
    target_vpc_subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet through which you want to route traffic. The specified subnet must be an existing target network of the Client VPN endpoint.</p> <p>Alternatively, if you're adding a route for the local network, specify <code>local</code>.</p> <p>This parameter is required for VPC-based Client VPN endpoints. For Transit Gateway-based endpoints, this parameter is not required.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the route.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
