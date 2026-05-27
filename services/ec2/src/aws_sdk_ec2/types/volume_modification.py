"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeModification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_modification_state
    import aws_sdk_ec2.types.volume_type


class VolumeModification(TypedDict):
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""
    modification_state: NotRequired[
        "aws_sdk_ec2.types.volume_modification_state.VolumeModificationState"
    ]
    """<p>The current modification state.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A status message about the modification progress or failure.</p>"""
    target_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The target size of the volume, in GiB.</p>"""
    target_iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The target IOPS rate of the volume.</p>"""
    target_volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The target EBS volume type of the volume.</p>"""
    target_throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The target throughput of the volume, in MiB/s.</p>"""
    target_multi_attach_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The target setting for Amazon EBS Multi-Attach.</p>"""
    original_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The original size of the volume, in GiB.</p>"""
    original_iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The original IOPS rate of the volume.</p>"""
    original_volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The original EBS volume type of the volume.</p>"""
    original_throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The original throughput of the volume, in MiB/s.</p>"""
    original_multi_attach_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The original setting for Amazon EBS Multi-Attach.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The modification progress, from 0 to 100 percent complete.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The modification start time.</p>"""
    end_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The modification completion or failure time.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
