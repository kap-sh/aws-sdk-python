"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshotsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.owner_string_list
    import aws_sdk_ec2.types.restorable_by_string_list
    import aws_sdk_ec2.types.snapshot_id_string_list
    import aws_sdk_ec2.types.string


class DescribeSnapshotsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    owner_ids: NotRequired["aws_sdk_ec2.types.owner_string_list.OwnerStringList"]
    """<p>Scopes the results to snapshots with the specified owners. You can specify a combination of Amazon Web Services account IDs, <code>self</code>, and <code>amazon</code>.</p>"""
    restorable_by_user_ids: NotRequired[
        "aws_sdk_ec2.types.restorable_by_string_list.RestorableByStringList"
    ]
    """<p>The IDs of the Amazon Web Services accounts that can create volumes from the snapshot.</p>"""
    snapshot_ids: NotRequired[
        "aws_sdk_ec2.types.snapshot_id_string_list.SnapshotIdStringList"
    ]
    """<p>The snapshot IDs.</p> <p>Default: Describes the snapshots for which you have create volume permissions.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>description</code> - A description of the snapshot.</p> </li> <li> <p> <code>encrypted</code> - Indicates whether the snapshot is encrypted (<code>true</code> | <code>false</code>)</p> </li> <li> <p> <code>owner-alias</code> - The owner alias, from an Amazon-maintained list (<code>amazon</code>). This is not the user-configured Amazon Web Services account alias set using the IAM console. We recommend that you use the related parameter instead of this filter.</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the owner. We recommend that you use the related parameter instead of this filter.</p> </li> <li> <p> <code>progress</code> - The progress of the snapshot, as a percentage (for example, 80%).</p> </li> <li> <p> <code>snapshot-id</code> - The snapshot ID.</p> </li> <li> <p> <code>start-time</code> - The time stamp when the snapshot was initiated.</p> </li> <li> <p> <code>status</code> - The status of the snapshot (<code>pending</code> | <code>completed</code> | <code>error</code>).</p> </li> <li> <p> <code>storage-tier</code> - The storage tier of the snapshot (<code>archive</code> | <code>standard</code>).</p> </li> <li> <p> <code>transfer-type</code> - The type of operation used to create the snapshot (<code>time-based</code> | <code>standard</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>volume-id</code> - The ID of the volume the snapshot is for.</p> </li> <li> <p> <code>volume-size</code> - The size of the volume, in GiB.</p> </li> </ul>"""
