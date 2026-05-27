"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_block_ids
    import aws_sdk_ec2.types.describe_capacity_block_status_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockStatusRequest(TypedDict):
    capacity_block_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_block_ids.CapacityBlockIds"
    ]
    """<p>The ID of the Capacity Block.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_block_status_max_results.DescribeCapacityBlockStatusMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. </p> <ul> <li> <p> <code>interconnect-status</code> - The status of the interconnect for the Capacity Block (<code>ok</code> | <code>impaired</code> | <code>insufficient-data</code>).</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
