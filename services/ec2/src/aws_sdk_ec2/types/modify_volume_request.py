"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.volume_id
    import aws_sdk_ec2.types.volume_type


class ModifyVolumeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume.</p>"""
    size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The target size of the volume, in GiB. The target volume size must be greater than or equal to the existing size of the volume.</p> <p>The following are the supported volumes sizes for each volume type:</p> <ul> <li> <p> <code>gp2</code>: 1 - 16,384 GiB</p> </li> <li> <p> <code>gp3</code>: 1 - 65,536 GiB</p> </li> <li> <p> <code>io1</code>: 4 - 16,384 GiB</p> </li> <li> <p> <code>io2</code>: 4 - 65,536 GiB</p> </li> <li> <p> <code>st1</code> and <code>sc1</code>: 125 - 16,384 GiB</p> </li> <li> <p> <code>standard</code>: 1 - 1024 GiB</p> </li> </ul> <p>Default: The existing size is retained.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The target EBS volume type of the volume. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html\">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Default: The existing type is retained.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The target IOPS rate of the volume. This parameter is valid only for <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes.</p> <p>The following are the supported values for each volume type:</p> <ul> <li> <p> <code>gp3</code>: 3,000 - 80,000 IOPS</p> </li> <li> <p> <code>io1</code>: 100 - 64,000 IOPS</p> </li> <li> <p> <code>io2</code>: 100 - 256,000 IOPS</p> </li> </ul> <note> <p> <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html\"> Instances built on the Nitro System</a> can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.</p> </note> <p>Default: The existing value is retained if you keep the same volume type. If you change the volume type to <code>io1</code>, <code>io2</code>, or <code>gp3</code>, the default is 3,000.</p>"""
    throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The target throughput of the volume, in MiB/s. This parameter is valid only for <code>gp3</code> volumes. The maximum value is 2,000.</p> <p>Default: The existing value is retained if the source and target volume type is <code>gp3</code>. Otherwise, the default value is 125.</p> <p>Valid Range: Minimum value of 125. Maximum value of 2,000.</p>"""
    multi_attach_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16 <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html\"> Nitro-based instances</a> in the same Availability Zone. This parameter is supported with <code>io1</code> and <code>io2</code> volumes only. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html\"> Amazon EBS Multi-Attach</a> in the <i>Amazon EBS User Guide</i>.</p>"""
