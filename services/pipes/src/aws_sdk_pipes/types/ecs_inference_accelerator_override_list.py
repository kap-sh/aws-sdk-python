"""Generated from Smithy shape ``com.amazonaws.pipes#EcsInferenceAcceleratorOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.ecs_inference_accelerator_override

EcsInferenceAcceleratorOverrideList: TypeAlias = list[
    "aws_sdk_pipes.types.ecs_inference_accelerator_override.EcsInferenceAcceleratorOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsInferenceAcceleratorOverrideList) -> list:
    import aws_sdk_pipes.types.ecs_inference_accelerator_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pipes.types.ecs_inference_accelerator_override.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EcsInferenceAcceleratorOverrideList:
    import aws_sdk_pipes.types.ecs_inference_accelerator_override

    out: EcsInferenceAcceleratorOverrideList = []
    for item in data:
        out.append(
            aws_sdk_pipes.types.ecs_inference_accelerator_override.deserialize_json(
                item
            )
        )
    return out
