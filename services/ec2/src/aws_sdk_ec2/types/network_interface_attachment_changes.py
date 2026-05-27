"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceAttachmentChanges``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_interface_attachment_id


class NetworkInterfaceAttachmentChanges(TypedDict):
    default_ena_queue_count: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The default number of the ENA queues.</p>"""
    ena_queue_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of ENA queues to be created with the instance.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_attachment_id.NetworkInterfaceAttachmentId"
    ]
    """<p>The ID of the network interface attachment.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
