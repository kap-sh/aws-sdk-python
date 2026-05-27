"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeOptionValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type_option_value

ResourceTypeOptionValuesList: TypeAlias = list[
    "aws_sdk_ec2.types.resource_type_option_value.ResourceTypeOptionValue"
]
