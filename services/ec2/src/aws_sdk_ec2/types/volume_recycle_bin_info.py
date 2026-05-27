"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeRecycleBinInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_id
    import aws_sdk_ec2.types.volume_state
    import aws_sdk_ec2.types.volume_type


class VolumeRecycleBinInfo(TypedDict):
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The volume type.</p>"""
    state: NotRequired["aws_sdk_ec2.types.volume_state.VolumeState"]
    """<p>The state of the volume.</p>"""
    size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) for the volume.</p>"""
    throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the volume is stored. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-outposts.html\">Amazon EBS volumes on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the volume.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone for the volume.</p>"""
    source_volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the source volume.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The snapshot from which the volume was created, if applicable.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the volume.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time stamp when volume creation was initiated.</p>"""
    recycle_bin_enter_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the volume entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the volume is to be permanently deleted from the Recycle Bin.</p>"""
