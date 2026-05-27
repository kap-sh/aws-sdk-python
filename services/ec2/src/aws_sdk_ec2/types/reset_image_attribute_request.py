"""Generated from Smithy shape ``com.amazonaws.ec2#ResetImageAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.reset_image_attribute_name


class ResetImageAttributeRequest(TypedDict):
    attribute: NotRequired[
        "aws_sdk_ec2.types.reset_image_attribute_name.ResetImageAttributeName"
    ]
    """<p>The attribute to reset (currently you can only reset the launch permission attribute).</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
