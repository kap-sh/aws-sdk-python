"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVpcAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.local_gateway_max_results
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayRouteTableVpcAssociationsRequest(TypedDict):
    local_gateway_route_table_vpc_association_ids: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id_set.LocalGatewayRouteTableVpcAssociationIdSet"
    ]
    """<p>The IDs of the associations.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>local-gateway-id</code> - The ID of a local gateway.</p> </li> <li> <p> <code>local-gateway-route-table-arn</code> - The Amazon Resource Name (ARN) of the local gateway route table for the association.</p> </li> <li> <p> <code>local-gateway-route-table-id</code> - The ID of the local gateway route table.</p> </li> <li> <p> <code>local-gateway-route-table-vpc-association-id</code> - The ID of the association.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the local gateway route table for the association.</p> </li> <li> <p> <code>state</code> - The state of the association.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.local_gateway_max_results.LocalGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
