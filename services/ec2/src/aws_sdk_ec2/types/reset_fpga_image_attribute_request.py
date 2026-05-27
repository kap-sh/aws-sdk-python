"""Generated from Smithy shape ``com.amazonaws.ec2#ResetFpgaImageAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fpga_image_id
    import aws_sdk_ec2.types.reset_fpga_image_attribute_name


class ResetFpgaImageAttributeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fpga_image_id: NotRequired["aws_sdk_ec2.types.fpga_image_id.FpgaImageId"]
    """<p>The ID of the AFI.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.reset_fpga_image_attribute_name.ResetFpgaImageAttributeName"
    ]
    """<p>The attribute.</p>"""
