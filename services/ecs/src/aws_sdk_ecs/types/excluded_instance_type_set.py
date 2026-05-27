"""Generated from Smithy shape ``com.amazonaws.ecs#ExcludedInstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.excluded_instance_type

ExcludedInstanceTypeSet: TypeAlias = list[
    "aws_sdk_ecs.types.excluded_instance_type.ExcludedInstanceType"
]
