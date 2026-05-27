"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageReferencesImageIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id

DescribeImageReferencesImageIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.image_id.ImageId"
]
