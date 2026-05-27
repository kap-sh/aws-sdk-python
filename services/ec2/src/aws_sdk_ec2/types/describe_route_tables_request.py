"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteTablesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_route_tables_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.route_table_id_string_list
    import aws_sdk_ec2.types.string


class DescribeRouteTablesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_route_tables_max_results.DescribeRouteTablesMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    route_table_ids: NotRequired[
        "aws_sdk_ec2.types.route_table_id_string_list.RouteTableIdStringList"
    ]
    """<p>The IDs of the route tables.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>association.gateway-id</code> - The ID of the gateway involved in the association.</p> </li> <li> <p> <code>association.route-table-association-id</code> - The ID of an association ID for the route table.</p> </li> <li> <p> <code>association.route-table-id</code> - The ID of the route table involved in the association.</p> </li> <li> <p> <code>association.subnet-id</code> - The ID of the subnet involved in the association.</p> </li> <li> <p> <code>association.main</code> - Indicates whether the route table is the main route table for the VPC (<code>true</code> | <code>false</code>). Route tables that do not have an association ID are not returned in the response.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the route table.</p> </li> <li> <p> <code>route-table-id</code> - The ID of the route table.</p> </li> <li> <p> <code>route.destination-cidr-block</code> - The IPv4 CIDR range specified in a route in the table.</p> </li> <li> <p> <code>route.destination-ipv6-cidr-block</code> - The IPv6 CIDR range specified in a route in the route table.</p> </li> <li> <p> <code>route.destination-prefix-list-id</code> - The ID (prefix) of the Amazon Web Services service specified in a route in the table.</p> </li> <li> <p> <code>route.egress-only-internet-gateway-id</code> - The ID of an egress-only Internet gateway specified in a route in the route table.</p> </li> <li> <p> <code>route.gateway-id</code> - The ID of a gateway specified in a route in the table.</p> </li> <li> <p> <code>route.instance-id</code> - The ID of an instance specified in a route in the table.</p> </li> <li> <p> <code>route.nat-gateway-id</code> - The ID of a NAT gateway.</p> </li> <li> <p> <code>route.transit-gateway-id</code> - The ID of a transit gateway.</p> </li> <li> <p> <code>route.origin</code> - Describes how the route was created. <code>CreateRouteTable</code> indicates that the route was automatically created when the route table was created; <code>CreateRoute</code> indicates that the route was manually added to the route table; <code>EnableVgwRoutePropagation</code> indicates that the route was propagated by route propagation.</p> </li> <li> <p> <code>route.state</code> - The state of a route in the route table (<code>active</code> | <code>blackhole</code>). The blackhole state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, the specified NAT instance has been terminated, and so on).</p> </li> <li> <p> <code>route.vpc-peering-connection-id</code> - The ID of a VPC peering connection specified in a route in the table.</p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC for the route table.</p> </li> </ul>"""
