"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesEbs``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.string


class ScheduledInstancesEbs(TypedDict):
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is deleted on instance termination.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is encrypted. You can attached encrypted volumes only to instances that support them.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) to provision for a <code>gp3</code>, <code>io1</code>, or <code>io2</code> volume.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p> <p>Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The volume type.</p> <p>Default: <code>gp2</code> </p>"""
