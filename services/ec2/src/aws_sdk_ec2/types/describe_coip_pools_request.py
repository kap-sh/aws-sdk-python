"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCoipPoolsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.coip_pool_id_set
    import aws_sdk_ec2.types.coip_pool_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCoipPoolsRequest(TypedDict):
    pool_ids: NotRequired["aws_sdk_ec2.types.coip_pool_id_set.CoipPoolIdSet"]
    """<p>The IDs of the address pools.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>coip-pool.local-gateway-route-table-id</code> - The ID of the local gateway route table.</p> </li> <li> <p> <code>coip-pool.pool-id</code> - The ID of the address pool.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.coip_pool_max_results.CoipPoolMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
