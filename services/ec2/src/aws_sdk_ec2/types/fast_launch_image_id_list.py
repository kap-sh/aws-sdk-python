"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchImageIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id

FastLaunchImageIdList: TypeAlias = list["aws_sdk_ec2.types.image_id.ImageId"]
