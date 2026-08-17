"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAcceleratorOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.inference_accelerator_override

InferenceAcceleratorOverrides: TypeAlias = list[
    "capo_ecs.types.inference_accelerator_override.InferenceAcceleratorOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceAcceleratorOverrides) -> list:
    import capo_ecs.types.inference_accelerator_override

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.inference_accelerator_override.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceAcceleratorOverrides:
    import capo_ecs.types.inference_accelerator_override

    out: InferenceAcceleratorOverrides = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.inference_accelerator_override.deserialize_aws_json_1_1(item)
        )
    return out
