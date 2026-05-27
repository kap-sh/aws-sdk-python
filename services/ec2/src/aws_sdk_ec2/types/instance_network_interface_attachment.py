"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceAttachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attachment_status
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_attachment_ena_srd_specification
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class InstanceNetworkInterfaceAttachment(TypedDict):
    attach_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the attachment initiated.</p>"""
    attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface attachment.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
    device_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the device on the instance for the network interface attachment.</p>"""
    status: NotRequired["aws_sdk_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The attachment state.</p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""
    ena_srd_specification: NotRequired[
        "aws_sdk_ec2.types.instance_attachment_ena_srd_specification.InstanceAttachmentEnaSrdSpecification"
    ]
    """<p>Contains the ENA Express settings for the network interface that's attached to the instance.</p>"""
    ena_queue_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of ENA queues created with the instance.</p>"""
