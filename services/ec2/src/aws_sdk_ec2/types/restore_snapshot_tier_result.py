"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotTierResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class RestoreSnapshotTierResult(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    restore_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the snapshot restore process started.</p>"""
    restore_duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>For temporary restores only. The number of days for which the archived snapshot is temporarily restored.</p>"""
    is_permanent_restore: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is permanently restored. <code>true</code> indicates a permanent restore. <code>false</code> indicates a temporary restore.</p>"""
