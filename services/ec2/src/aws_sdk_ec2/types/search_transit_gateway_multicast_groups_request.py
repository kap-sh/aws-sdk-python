"""Generated from Smithy shape ``com.amazonaws.ec2#SearchTransitGatewayMulticastGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_max_results
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_id


class SearchTransitGatewayMulticastGroupsRequest(TypedDict):
    transit_gateway_multicast_domain_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
    ]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>group-ip-address</code> - The IP address of the transit gateway multicast group.</p> </li> <li> <p> <code>is-group-member</code> - The resource is a group member. Valid values are <code>true</code> | <code>false</code>.</p> </li> <li> <p> <code>is-group-source</code> - The resource is a group source. Valid values are <code>true</code> | <code>false</code>.</p> </li> <li> <p> <code>member-type</code> - The member type. Valid values are <code>igmp</code> | <code>static</code>.</p> </li> <li> <p> <code>resource-id</code> - The ID of the resource.</p> </li> <li> <p> <code>resource-type</code> - The type of resource. Valid values are <code>vpc</code> | <code>vpn</code> | <code>direct-connect-gateway</code> | <code>tgw-peering</code>.</p> </li> <li> <p> <code>source-type</code> - The source type. Valid values are <code>igmp</code> | <code>static</code>.</p> </li> <li> <p> <code>subnet-id</code> - The ID of the subnet.</p> </li> <li> <p> <code>transit-gateway-attachment-id</code> - The id of the transit gateway attachment.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
