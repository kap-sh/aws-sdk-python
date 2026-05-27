"""Generated from Smithy shape ``com.amazonaws.ec2#Volume``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.sse_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.volume_attachment_list
    import aws_sdk_ec2.types.volume_state
    import aws_sdk_ec2.types.volume_type


class Volume(TypedDict):
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone for the volume.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    source_volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the source volume from which the volume copy was created. Only for volume copies.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the volume.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The volume type.</p>"""
    fast_restored: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<note> <p>This parameter is not returned by CreateVolume.</p> </note> <p>Indicates whether the volume was created using fast snapshot restore.</p>"""
    multi_attach_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether Amazon EBS Multi-Attach is enabled.</p>"""
    throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    sse_type: NotRequired["aws_sdk_ec2.types.sse_type.SSEType"]
    """<note> <p>This parameter is not returned by CreateVolume.</p> </note> <p>Reserved for future use.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the volume.</p>"""
    volume_initialization_rate: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume during creation, in MiB/s. If no volume initialization rate was specified, the value is <code>null</code>.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""
    size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiBs.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The snapshot from which the volume was created, if applicable.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the volume.</p>"""
    state: NotRequired["aws_sdk_ec2.types.volume_state.VolumeState"]
    """<p>The volume state.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time stamp when volume creation was initiated.</p>"""
    attachments: NotRequired[
        "aws_sdk_ec2.types.volume_attachment_list.VolumeAttachmentList"
    ]
    """<note> <p>This parameter is not returned by CreateVolume.</p> </note> <p>Information about the volume attachments.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is encrypted.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that was used to protect the volume encryption key for the volume.</p>"""
