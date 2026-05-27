"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFpgaImagesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image_list
    import aws_sdk_ec2.types.next_token


class DescribeFpgaImagesResult(TypedDict):
    fpga_images: NotRequired["aws_sdk_ec2.types.fpga_image_list.FpgaImageList"]
    """<p>Information about the FPGA images.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
