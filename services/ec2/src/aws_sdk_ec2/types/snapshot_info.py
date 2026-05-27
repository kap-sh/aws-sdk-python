"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.snapshot_state
    import aws_sdk_ec2.types.sse_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SnapshotInfo(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Description specified by the CreateSnapshotRequest that has been applied to all snapshots.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Tags associated with this snapshot.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Source volume from which this snapshot was created.</p>"""
    state: NotRequired["aws_sdk_ec2.types.snapshot_state.SnapshotState"]
    """<p>Current state of the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Size of the volume from which this snapshot was created.</p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Time this snapshot was started. This is the same for all snapshots initiated by the same request.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Progress this snapshot has made towards completing.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Account id used when creating this snapshot.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Snapshot id that can be used to describe this snapshot.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the snapshot is stored. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html\">Amazon EBS local snapshots on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    sse_type: NotRequired["aws_sdk_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone of the snapshots. For example, <code>us-west-1a</code> (Availability Zone) or <code>us-west-2-lax-1a</code> (Local Zone).</p>"""
