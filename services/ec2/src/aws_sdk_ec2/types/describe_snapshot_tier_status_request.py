"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshotTierStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_snapshot_tier_status_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeSnapshotTierStatusRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>snapshot-id</code> - The snapshot ID.</p> </li> <li> <p> <code>volume-id</code> - The ID of the volume the snapshot is for.</p> </li> <li> <p> <code>last-tiering-operation</code> - The state of the last archive or restore action. (<code>archival-in-progress</code> | <code>archival-completed</code> | <code>archival-failed</code> | <code>permanent-restore-in-progress</code> | <code>permanent-restore-completed</code> | <code>permanent-restore-failed</code> | <code>temporary-restore-in-progress</code> | <code>temporary-restore-completed</code> | <code>temporary-restore-failed</code>)</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_snapshot_tier_status_max_results.DescribeSnapshotTierStatusMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
