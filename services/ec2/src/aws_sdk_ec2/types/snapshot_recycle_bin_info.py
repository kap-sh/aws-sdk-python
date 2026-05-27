"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotRecycleBinInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class SnapshotRecycleBinInfo(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    recycle_bin_enter_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the snapshot entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the snapshot is to be permanently deleted from the Recycle Bin.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the snapshot.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume from which the snapshot was created.</p>"""
