"""Generated from Smithy shape ``com.amazonaws.ec2#EbsBlockDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.volume_type


class EbsBlockDeviceResponse(TypedDict):
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is encrypted.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is deleted on instance termination.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.</p>"""
    throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiBs.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The volume type. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html\">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p>"""
