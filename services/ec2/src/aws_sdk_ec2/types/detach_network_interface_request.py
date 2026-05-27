"""Generated from Smithy shape ``com.amazonaws.ec2#DetachNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_interface_attachment_id


class DetachNetworkInterfaceRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_attachment_id.NetworkInterfaceAttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    force: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to force a detachment.</p> <note> <ul> <li> <p>Use the <code>Force</code> parameter only as a last resort to detach a network interface from a failed instance. </p> </li> <li> <p>If you use the <code>Force</code> parameter to detach a network interface, you might not be able to attach a different network interface to the same index on the instance without first stopping and starting the instance.</p> </li> <li> <p>If you force the detachment of a network interface, the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html\">instance metadata</a> might not get updated. This means that the attributes associated with the detached network interface might still be visible. The instance metadata will get updated when you stop and start the instance.</p> </li> </ul> </note>"""
