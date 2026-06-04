"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAcceleratorOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.inference_accelerator_override

InferenceAcceleratorOverrides: TypeAlias = list[
    "aws_sdk_ecs.types.inference_accelerator_override.InferenceAcceleratorOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceAcceleratorOverrides) -> list:
    import aws_sdk_ecs.types.inference_accelerator_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.inference_accelerator_override.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceAcceleratorOverrides:
    import aws_sdk_ecs.types.inference_accelerator_override

    out: InferenceAcceleratorOverrides = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.inference_accelerator_override.deserialize_aws_json_1_1(
                item
            )
        )
    return out
