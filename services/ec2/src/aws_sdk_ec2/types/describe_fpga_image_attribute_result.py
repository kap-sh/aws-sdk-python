"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFpgaImageAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image_attribute


class DescribeFpgaImageAttributeResult(TypedDict):
    fpga_image_attribute: NotRequired[
        "aws_sdk_ec2.types.fpga_image_attribute.FpgaImageAttribute"
    ]
    """<p>Information about the attribute.</p>"""
