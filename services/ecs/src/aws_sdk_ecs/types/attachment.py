"""Generated from Smithy shape ``com.amazonaws.ecs#Attachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attachment_details
    import aws_sdk_ecs.types.string


class Attachment(TypedDict):
    id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The unique identifier for the attachment.</p>"""
    type: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The type of the attachment, such as <code>ElasticNetworkInterface</code>, <code>Service Connect</code>, and <code>AmazonElasticBlockStorage</code>.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> The status of the attachment. Valid values are <code>PRECREATED</code>, <code>CREATED</code>, <code>ATTACHING</code>, <code>ATTACHED</code>, <code>DETACHING</code>, <code>DETACHED</code>, <code>DELETED</code>, and <code>FAILED</code>.</p>"""
    details: NotRequired["aws_sdk_ecs.types.attachment_details.AttachmentDetails"]
    """<p>Details of the attachment.</p> <p>For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.</p> <p>For Service Connect services, this includes <code>portName</code>, <code>clientAliases</code>, <code>discoveryName</code>, and <code>ingressPortOverride</code>.</p> <p>For Elastic Block Storage, this includes <code>roleArn</code>, <code>deleteOnTermination</code>, <code>volumeName</code>, <code>volumeId</code>, and <code>statusReason</code> (only when the attachment fails to create or attach).</p>"""
