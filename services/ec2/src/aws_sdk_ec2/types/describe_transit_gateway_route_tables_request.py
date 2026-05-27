"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayRouteTablesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_max_results
    import aws_sdk_ec2.types.transit_gateway_route_table_id_string_list


class DescribeTransitGatewayRouteTablesRequest(TypedDict):
    transit_gateway_route_table_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id_string_list.TransitGatewayRouteTableIdStringList"
    ]
    """<p>The IDs of the transit gateway route tables.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>default-association-route-table</code> - Indicates whether this is the default association route table for the transit gateway (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>default-propagation-route-table</code> - Indicates whether this is the default propagation route table for the transit gateway (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>state</code> - The state of the route table (<code>available</code> | <code>deleting</code> | <code>deleted</code> | <code>pending</code>).</p> </li> <li> <p> <code>transit-gateway-id</code> - The ID of the transit gateway.</p> </li> <li> <p> <code>transit-gateway-route-table-id</code> - The ID of the transit gateway route table.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
