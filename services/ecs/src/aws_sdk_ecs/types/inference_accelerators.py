"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAccelerators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.inference_accelerator

InferenceAccelerators: TypeAlias = list[
    "aws_sdk_ecs.types.inference_accelerator.InferenceAccelerator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceAccelerators) -> list:
    import aws_sdk_ecs.types.inference_accelerator

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.inference_accelerator.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceAccelerators:
    import aws_sdk_ecs.types.inference_accelerator

    out: InferenceAccelerators = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.inference_accelerator.deserialize_aws_json_1_1(item)
        )
    return out
