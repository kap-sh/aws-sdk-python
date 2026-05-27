"""Generated from Smithy shape ``com.amazonaws.ec2#CreateReplaceRootVolumeTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateReplaceRootVolumeTaskRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance for which to replace the root volume.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot from which to restore the replacement root volume. The specified snapshot must be a snapshot that you previously created from the original root volume.</p> <p>If you want to restore the replacement root volume to the initial launch state, or if you want to restore the replacement root volume from an AMI, omit this parameter.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the root volume replacement task.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI to use to restore the root volume. The specified AMI must have the same product code, billing information, architecture type, and virtualization type as that of the instance.</p> <p>If you want to restore the replacement volume from a specific snapshot, or if you want to restore it to its launch state, omit this parameter.</p>"""
    delete_replaced_root_volume: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to automatically delete the original root volume after the root volume replacement task completes. To delete the original root volume, specify <code>true</code>. If you choose to keep the original root volume after the replacement task completes, you must manually delete it when you no longer need it.</p>"""
    volume_initialization_rate: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the replacement root volume. This is also known as <i>volume initialization</i>. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.</p> <p>Omit this parameter if:</p> <ul> <li> <p>You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.</p> <note> <p>If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.</p> </note> </li> <li> <p>You want to create a volume that is initialized at the default rate.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html\"> Initialize Amazon EBS volumes</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Valid range: 100 - 300 MiB/s</p>"""
