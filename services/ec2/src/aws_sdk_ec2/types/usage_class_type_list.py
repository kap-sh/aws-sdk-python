"""Generated from Smithy shape ``com.amazonaws.ec2#UsageClassTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.usage_class_type

UsageClassTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.usage_class_type.UsageClassType"
]
