"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorNameSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.accelerator_name

AcceleratorNameSet: TypeAlias = list[
    "aws_sdk_ecs.types.accelerator_name.AcceleratorName"
]
