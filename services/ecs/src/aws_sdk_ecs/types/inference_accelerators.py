"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAccelerators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.inference_accelerator

InferenceAccelerators: TypeAlias = list[
    "aws_sdk_ecs.types.inference_accelerator.InferenceAccelerator"
]
