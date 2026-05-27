"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAcceleratorOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.inference_accelerator_override

InferenceAcceleratorOverrides: TypeAlias = list[
    "aws_sdk_ecs.types.inference_accelerator_override.InferenceAcceleratorOverride"
]
