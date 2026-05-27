"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeOptionValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_resource_type_option_value

ImageUsageResourceTypeOptionValuesList: TypeAlias = list[
    "aws_sdk_ec2.types.image_usage_resource_type_option_value.ImageUsageResourceTypeOptionValue"
]
