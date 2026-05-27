"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFpgaImageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CreateFpgaImageResult(TypedDict):
    fpga_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The FPGA image identifier (AFI ID).</p>"""
    fpga_image_global_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The global FPGA image identifier (AGFI ID).</p>"""
