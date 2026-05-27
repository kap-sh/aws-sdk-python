"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeServiceLinkVirtualInterfacesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.service_link_max_results
    import aws_sdk_ec2.types.service_link_virtual_interface_id_set
    import aws_sdk_ec2.types.string


class DescribeServiceLinkVirtualInterfacesRequest(TypedDict):
    service_link_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_id_set.ServiceLinkVirtualInterfaceIdSet"
    ]
    """<p>The IDs of the service link virtual interfaces.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters to use for narrowing down the request. The following filters are supported:</p> <ul> <li> <p> <code>outpost-lag-id</code> - The ID of the Outpost LAG.</p> </li> <li> <p> <code>outpost-arn</code> - The Outpost ARN.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the service link virtual interface.</p> </li> <li> <p> <code>state</code> - The state of the Outpost LAG.</p> </li> <li> <p> <code>vlan</code> - The ID of the address pool.</p> </li> <li> <p> <code>service-link-virtual-interface-id</code> - The ID of the service link virtual interface.</p> </li> <li> <p> <code>local-gateway-virtual-interface-id</code> - The ID of the local gateway virtual interface.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.service_link_max_results.ServiceLinkMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
