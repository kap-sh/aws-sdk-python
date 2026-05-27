"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayVirtualInterfaceGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.local_gateway_max_results
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayVirtualInterfaceGroupsRequest(TypedDict):
    local_gateway_virtual_interface_group_ids: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id_set.LocalGatewayVirtualInterfaceGroupIdSet"
    ]
    """<p>The IDs of the virtual interface groups.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>local-gateway-id</code> - The ID of a local gateway.</p> </li> <li> <p> <code>local-gateway-virtual-interface-group-id</code> - The ID of the virtual interface group.</p> </li> <li> <p> <code>local-gateway-virtual-interface-id</code> - The ID of the virtual interface.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the local gateway virtual interface group.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.local_gateway_max_results.LocalGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
