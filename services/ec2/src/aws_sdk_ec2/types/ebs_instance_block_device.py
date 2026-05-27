"""Generated from Smithy shape ``com.amazonaws.ec2#EbsInstanceBlockDevice``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attachment_status
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string


class EbsInstanceBlockDevice(TypedDict):
    attach_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the attachment initiated.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is deleted on instance termination.</p>"""
    status: NotRequired["aws_sdk_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The attachment state.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the EBS volume.</p>"""
    associated_resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Amazon Web Services-managed resource to which the volume is attached.</p>"""
    volume_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the volume.</p> <p>This parameter is returned only for volumes that are attached to Amazon Web Services-managed resources.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the EBS volume.</p>"""
    ebs_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""
