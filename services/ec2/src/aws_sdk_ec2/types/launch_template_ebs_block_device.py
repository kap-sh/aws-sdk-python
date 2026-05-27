"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateEbsBlockDevice``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.volume_type


class LaunchTemplateEbsBlockDevice(TypedDict):
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is encrypted.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is deleted on instance termination.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) that the volume supports. </p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The volume type.</p>"""
    throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    volume_initialization_rate: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume, in MiB/s. If no volume initialization rate was specified, the value is <code>null</code>.</p>"""
    ebs_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""
