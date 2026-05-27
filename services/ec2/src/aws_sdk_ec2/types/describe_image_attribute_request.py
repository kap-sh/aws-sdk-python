"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_attribute_name
    import aws_sdk_ec2.types.image_id


class DescribeImageAttributeRequest(TypedDict):
    attribute: NotRequired["aws_sdk_ec2.types.image_attribute_name.ImageAttributeName"]
    """<p>The AMI attribute.</p> <p> <b>Note</b>: The <code>blockDeviceMapping</code> attribute is deprecated. Using this attribute returns the <code>Client.AuthFailure</code> error. To get information about the block device mappings for an AMI, describe the image instead.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
