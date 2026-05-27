"""Generated from Smithy shape ``com.amazonaws.ec2#GetCoipPoolUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.coip_pool_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.ipv4_pool_coip_id
    import aws_sdk_ec2.types.string


class GetCoipPoolUsageRequest(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p>The ID of the address pool.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>coip-address-usage.allocation-id</code> - The allocation ID of the address.</p> </li> <li> <p> <code>coip-address-usage.aws-account-id</code> - The ID of the Amazon Web Services account that is using the customer-owned IP address.</p> </li> <li> <p> <code>coip-address-usage.aws-service</code> - The Amazon Web Services service that is using the customer-owned IP address.</p> </li> <li> <p> <code>coip-address-usage.co-ip</code> - The customer-owned IP address.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.coip_pool_max_results.CoipPoolMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
