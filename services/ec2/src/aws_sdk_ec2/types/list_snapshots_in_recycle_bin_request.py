"""Generated from Smithy shape ``com.amazonaws.ec2#ListSnapshotsInRecycleBinRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.list_snapshots_in_recycle_bin_max_results
    import aws_sdk_ec2.types.snapshot_id_string_list
    import aws_sdk_ec2.types.string


class ListSnapshotsInRecycleBinRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_ec2.types.list_snapshots_in_recycle_bin_max_results.ListSnapshotsInRecycleBinMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    snapshot_ids: NotRequired[
        "aws_sdk_ec2.types.snapshot_id_string_list.SnapshotIdStringList"
    ]
    """<p>The IDs of the snapshots to list. Omit this parameter to list all of the snapshots that are in the Recycle Bin.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
