"""Generated from Smithy shape ``com.amazonaws.ec2#AttachVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_integer
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_id


class AttachVolumeRequest(TypedDict):
    device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the EBS volume. The volume and instance must be within the same Availability Zone.</p>"""
    ebs_card_index: NotRequired["aws_sdk_ec2.types.boxed_integer.BoxedInteger"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
