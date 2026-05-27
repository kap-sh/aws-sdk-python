"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeAttachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_attachment_state


class VolumeAttachment(TypedDict):
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is deleted on instance termination.</p>"""
    associated_resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Amazon Web Services-managed resource to which the volume is attached.</p>"""
    instance_owning_service: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The service principal of the Amazon Web Services service that owns the underlying resource to which the volume is attached.</p> <p>This parameter is returned only for volumes that are attached to Amazon Web Services-managed resources.</p>"""
    ebs_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p> <p>If the volume is attached to an Amazon Web Services-managed resource, this parameter returns <code>null</code>.</p>"""
    device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name.</p> <p>If the volume is attached to an Amazon Web Services-managed resource, this parameter returns <code>null</code>.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.volume_attachment_state.VolumeAttachmentState"
    ]
    """<p>The attachment state of the volume.</p>"""
    attach_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the attachment initiated.</p>"""
