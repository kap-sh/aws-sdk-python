"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_resource_type_option

ImageUsageResourceTypeOptionList: TypeAlias = list[
    "aws_sdk_ec2.types.image_usage_resource_type_option.ImageUsageResourceTypeOption"
]
