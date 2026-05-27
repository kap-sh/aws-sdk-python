"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotFromRecycleBinResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.snapshot_state
    import aws_sdk_ec2.types.sse_type
    import aws_sdk_ec2.types.string


class RestoreSnapshotFromRecycleBinResult(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the snapshot is stored. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html\">Amazon EBS local snapshots on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the snapshot.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the EBS snapshot.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The progress of the snapshot, as a percentage.</p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time stamp when the snapshot was initiated.</p>"""
    state: NotRequired["aws_sdk_ec2.types.snapshot_state.SnapshotState"]
    """<p>The state of the snapshot.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume that was used to create the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    sse_type: NotRequired["aws_sdk_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""
