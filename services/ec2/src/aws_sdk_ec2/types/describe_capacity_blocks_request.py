"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlocksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_block_ids
    import aws_sdk_ec2.types.describe_capacity_blocks_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityBlocksRequest(TypedDict):
    capacity_block_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_block_ids.CapacityBlockIds"
    ]
    """<p>The IDs of the Capacity Blocks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_blocks_max_results.DescribeCapacityBlocksMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p> One or more filters. </p> <ul> <li> <p> <code>capacity-block-id</code> - The ID of the Capacity Block.</p> </li> <li> <p> <code>ultraserver-type</code> - The Capacity Block type. The type can be <code>instances</code> or <code>ultraservers</code>.</p> </li> <li> <p> <code>availability-zone</code> - The Availability Zone of the Capacity Block.</p> </li> <li> <p> <code>start-date</code> - The date and time at which the Capacity Block was started.</p> </li> <li> <p> <code>end-date</code> - The date and time at which the Capacity Block expires. When a Capacity Block expires, all instances in the Capacity Block are terminated.</p> </li> <li> <p> <code>create-date</code> - The date and time at which the Capacity Block was created.</p> </li> <li> <p> <code>state</code> - The state of the Capacity Block (<code>active</code> | <code>expired</code> | <code>unavailable</code> | <code>cancelled</code> | <code>failed</code> | <code>scheduled</code> | <code>payment-pending</code> | <code>payment-failed</code>).</p> </li> <li> <p> <code>tags</code> - The tags assigned to the Capacity Block.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
