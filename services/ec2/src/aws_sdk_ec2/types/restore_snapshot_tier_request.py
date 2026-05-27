"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotTierRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.restore_snapshot_tier_request_temporary_restore_days
    import aws_sdk_ec2.types.snapshot_id


class RestoreSnapshotTierRequest(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot to restore.</p>"""
    temporary_restore_days: NotRequired[
        "aws_sdk_ec2.types.restore_snapshot_tier_request_temporary_restore_days.RestoreSnapshotTierRequestTemporaryRestoreDays"
    ]
    """<p>Specifies the number of days for which to temporarily restore an archived snapshot. Required for temporary restores only. The snapshot will be automatically re-archived after this period.</p> <p>To temporarily restore an archived snapshot, specify the number of days and omit the <b>PermanentRestore</b> parameter or set it to <code>false</code>.</p>"""
    permanent_restore: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to permanently restore an archived snapshot. To permanently restore an archived snapshot, specify <code>true</code> and omit the <b>RestoreSnapshotTierRequest$TemporaryRestoreDays</b> parameter.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
