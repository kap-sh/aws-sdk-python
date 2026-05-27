"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.accelerator_type

AcceleratorTypeSet: TypeAlias = list[
    "aws_sdk_ecs.types.accelerator_type.AcceleratorType"
]
