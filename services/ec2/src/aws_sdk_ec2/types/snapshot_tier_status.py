"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotTierStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.snapshot_state
    import aws_sdk_ec2.types.storage_tier
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.tiering_operation_status
    import aws_sdk_ec2.types.volume_id


class SnapshotTierStatus(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume from which the snapshot was created.</p>"""
    status: NotRequired["aws_sdk_ec2.types.snapshot_state.SnapshotState"]
    """<p>The state of the snapshot.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the snapshot.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags that are assigned to the snapshot.</p>"""
    storage_tier: NotRequired["aws_sdk_ec2.types.storage_tier.StorageTier"]
    """<p>The storage tier in which the snapshot is stored. <code>standard</code> indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. <code>archive</code> indicates that the snapshot is currently archived and that it must be restored before it can be used.</p>"""
    last_tiering_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the last archive or restore process was started.</p>"""
    last_tiering_progress: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The progress of the last archive or restore process, as a percentage.</p>"""
    last_tiering_operation_status: NotRequired[
        "aws_sdk_ec2.types.tiering_operation_status.TieringOperationStatus"
    ]
    """<p>The status of the last archive or restore process.</p>"""
    last_tiering_operation_status_detail: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message describing the status of the last archive or restore process.</p>"""
    archival_complete_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the last archive process was completed.</p>"""
    restore_expiry_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived.</p>"""
