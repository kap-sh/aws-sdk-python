"""Generated from Smithy shape ``com.amazonaws.ec2#CopyFpgaImageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CopyFpgaImageResult(TypedDict):
    fpga_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the new AFI.</p>"""
