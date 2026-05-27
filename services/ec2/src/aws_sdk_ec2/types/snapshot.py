"""Generated from Smithy shape ``com.amazonaws.ec2#Snapshot``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.snapshot_completion_duration_minutes_response
    import aws_sdk_ec2.types.snapshot_state
    import aws_sdk_ec2.types.sse_type
    import aws_sdk_ec2.types.storage_tier
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transfer_type


class Snapshot(TypedDict):
    owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services owner alias, from an Amazon-maintained list (<code>amazon</code>). This is not the user-configured Amazon Web Services account alias set using the IAM console.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the snapshot is stored. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html\">Amazon EBS local snapshots on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the snapshot.</p>"""
    storage_tier: NotRequired["aws_sdk_ec2.types.storage_tier.StorageTier"]
    """<p>The storage tier in which the snapshot is stored. <code>standard</code> indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. <code>archive</code> indicates that the snapshot is currently archived and that it must be restored before it can be used.</p>"""
    restore_expiry_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived.</p>"""
    sse_type: NotRequired["aws_sdk_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone of the snapshot. For example, <code>us-west-1a</code> (Availability Zone) or <code>us-west-2-lax-1a</code> (Local Zone).</p>"""
    transfer_type: NotRequired["aws_sdk_ec2.types.transfer_type.TransferType"]
    """<note> <p>Only for snapshot copies.</p> </note> <p>Indicates whether the snapshot copy was created with a standard or time-based snapshot copy operation. Time-based snapshot copy operations complete within the completion duration specified in the request. Standard snapshot copy operations are completed on a best-effort basis.</p> <ul> <li> <p> <code>standard</code> - The snapshot copy was created with a standard snapshot copy operation.</p> </li> <li> <p> <code>time-based</code> - The snapshot copy was created with a time-based snapshot copy operation.</p> </li> </ul>"""
    completion_duration_minutes: NotRequired[
        "aws_sdk_ec2.types.snapshot_completion_duration_minutes_response.SnapshotCompletionDurationMinutesResponse"
    ]
    """<note> <p>Only for snapshot copies created with time-based snapshot copy operations.</p> </note> <p>The completion duration requested for the time-based snapshot copy operation.</p>"""
    completion_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time stamp when the snapshot was completed.</p>"""
    full_snapshot_size_in_bytes: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The full size of the snapshot, in bytes.</p> <important> <p>This is <b>not</b> the incremental size of the snapshot. This is the full snapshot size and represents the size of all the blocks that were written to the source volume at the time the snapshot was created.</p> </important>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot. Each snapshot receives a unique identifier when it is created.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume that was used to create the snapshot. Snapshots created by a copy snapshot operation have an arbitrary volume ID that you should not use for any purpose.</p>"""
    state: NotRequired["aws_sdk_ec2.types.snapshot_state.SnapshotState"]
    """<p>The snapshot state.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper KMS permissions are not obtained) this field displays error state details to help you diagnose why the error occurred. This parameter is only returned by <a>DescribeSnapshots</a>.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the snapshot was initiated.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The progress of the snapshot, as a percentage.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the EBS snapshot.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that was used to protect the volume encryption key for the parent volume.</p>"""
    data_encryption_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The data encryption key identifier for the snapshot. This value is a unique identifier that corresponds to the data encryption key that was used to encrypt the original volume or snapshot copy. Because data encryption keys are inherited by volumes created from snapshots, and vice versa, if snapshots share the same data encryption key identifier, then they belong to the same volume/snapshot lineage. This parameter is only returned by <a>DescribeSnapshots</a>.</p>"""
