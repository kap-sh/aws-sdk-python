"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastSnapshotRestoresRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_fast_snapshot_restores_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeFastSnapshotRestoresRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters. The possible values are:</p> <ul> <li> <p> <code>availability-zone</code>: The Availability Zone of the snapshot. For example, <code>us-east-2a</code>.</p> </li> <li> <p> <code>availability-zone-id</code>: The ID of the Availability Zone of the snapshot. For example, <code>use2-az1</code>.</p> </li> <li> <p> <code>owner-id</code>: The ID of the Amazon Web Services account that enabled fast snapshot restore on the snapshot.</p> </li> <li> <p> <code>snapshot-id</code>: The ID of the snapshot.</p> </li> <li> <p> <code>state</code>: The state of fast snapshot restores for the snapshot (<code>enabling</code> | <code>optimizing</code> | <code>enabled</code> | <code>disabling</code> | <code>disabled</code>).</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_fast_snapshot_restores_max_results.DescribeFastSnapshotRestoresMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
