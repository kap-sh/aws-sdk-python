"""Generated from Smithy shape ``com.amazonaws.ec2#ImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image

ImageList: TypeAlias = list["aws_sdk_ec2.types.image.Image"]
