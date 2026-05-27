"""Generated from Smithy shape ``com.amazonaws.ec2#SearchTransitGatewayRoutesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_max_results
    import aws_sdk_ec2.types.transit_gateway_route_table_id


class SearchTransitGatewayRoutesRequest(TypedDict):
    transit_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the transit gateway route table.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>attachment.transit-gateway-attachment-id</code>- The id of the transit gateway attachment.</p> </li> <li> <p> <code>attachment.resource-id</code> - The resource id of the transit gateway attachment.</p> </li> <li> <p> <code>attachment.resource-type</code> - The attachment resource type. Valid values are <code>vpc</code> | <code>vpn</code> | <code>direct-connect-gateway</code> | <code>peering</code> | <code>connect</code>.</p> </li> <li> <p> <code>prefix-list-id</code> - The ID of the prefix list.</p> </li> <li> <p> <code>route-search.exact-match</code> - The exact match of the specified filter.</p> </li> <li> <p> <code>route-search.longest-prefix-match</code> - The longest prefix that matches the route.</p> </li> <li> <p> <code>route-search.subnet-of-match</code> - The routes with a subnet that match the specified CIDR filter.</p> </li> <li> <p> <code>route-search.supernet-of-match</code> - The routes with a CIDR that encompass the CIDR filter. For example, if you have 10.0.1.0/29 and 10.0.1.0/31 routes in your route table and you specify supernet-of-match as 10.0.1.0/30, then the result returns 10.0.1.0/29.</p> </li> <li> <p> <code>state</code> - The state of the route (<code>active</code> | <code>blackhole</code>).</p> </li> <li> <p> <code>type</code> - The type of route (<code>propagated</code> | <code>static</code>).</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of routes to return. If a value is not provided, the default is 1000.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
