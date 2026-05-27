"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id


class DeregisterImageRequest(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    delete_associated_snapshots: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to delete the snapshots associated with the AMI during deregistration.</p> <note> <p>If a snapshot is associated with multiple AMIs, it is not deleted, regardless of this setting.</p> </note> <p>Default: The snapshots are not deleted.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
