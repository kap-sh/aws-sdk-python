"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupSourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_id
    import aws_sdk_ec2.types.transit_gateway_network_interface_id_list


class RegisterTransitGatewayMulticastGroupSourcesRequest(TypedDict):
    transit_gateway_multicast_domain_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
    ]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    group_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""
    network_interface_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_network_interface_id_list.TransitGatewayNetworkInterfaceIdList"
    ]
    """<p>The group sources' network interface IDs to register with the transit gateway multicast group.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
