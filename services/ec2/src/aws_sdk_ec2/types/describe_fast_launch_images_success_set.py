"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImagesSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fast_launch_images_success_item

DescribeFastLaunchImagesSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.describe_fast_launch_images_success_item.DescribeFastLaunchImagesSuccessItem"
]
