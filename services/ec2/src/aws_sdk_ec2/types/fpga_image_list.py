"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image

FpgaImageList: TypeAlias = list["aws_sdk_ec2.types.fpga_image.FpgaImage"]
