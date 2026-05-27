"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressTransfersRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_address_transfers_max_results
    import aws_sdk_ec2.types.string


class DescribeAddressTransfersRequest(TypedDict):
    allocation_ids: NotRequired["aws_sdk_ec2.types.allocation_id_list.AllocationIdList"]
    """<p>The allocation IDs of Elastic IP addresses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_address_transfers_max_results.DescribeAddressTransfersMaxResults"
    ]
    """<p>The maximum number of address transfers to return in one page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
