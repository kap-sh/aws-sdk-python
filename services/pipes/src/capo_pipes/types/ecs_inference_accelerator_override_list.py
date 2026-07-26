"""Generated from Smithy shape ``com.amazonaws.pipes#EcsInferenceAcceleratorOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.ecs_inference_accelerator_override

EcsInferenceAcceleratorOverrideList: TypeAlias = list[
    "capo_pipes.types.ecs_inference_accelerator_override.EcsInferenceAcceleratorOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsInferenceAcceleratorOverrideList) -> list:
    import capo_pipes.types.ecs_inference_accelerator_override

    out: list = []
    for item in value:
        out.append(
            capo_pipes.types.ecs_inference_accelerator_override.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EcsInferenceAcceleratorOverrideList:
    import capo_pipes.types.ecs_inference_accelerator_override

    out: EcsInferenceAcceleratorOverrideList = []
    for item in data:
        out.append(
            capo_pipes.types.ecs_inference_accelerator_override.deserialize_json(item)
        )
    return out
