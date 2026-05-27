"""Generated from Smithy shape ``com.amazonaws.ecs#AllowedInstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.allowed_instance_type

AllowedInstanceTypeSet: TypeAlias = list[
    "aws_sdk_ecs.types.allowed_instance_type.AllowedInstanceType"
]
