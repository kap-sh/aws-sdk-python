"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionInferenceAcceleratorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_details

AwsEcsTaskDefinitionInferenceAcceleratorsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_details.AwsEcsTaskDefinitionInferenceAcceleratorsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionInferenceAcceleratorsList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsTaskDefinitionInferenceAcceleratorsList:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_details

    out: AwsEcsTaskDefinitionInferenceAcceleratorsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_task_definition_inference_accelerators_details.deserialize_json(
                item
            )
        )
    return out
