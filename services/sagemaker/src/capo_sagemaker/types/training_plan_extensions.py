"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanExtensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_extension

TrainingPlanExtensions: TypeAlias = list[
    "capo_sagemaker.types.training_plan_extension.TrainingPlanExtension"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanExtensions) -> list:
    import capo_sagemaker.types.training_plan_extension

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_plan_extension.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingPlanExtensions:
    import capo_sagemaker.types.training_plan_extension

    out: TrainingPlanExtensions = []
    for item in data:
        out.append(
            capo_sagemaker.types.training_plan_extension.deserialize_aws_json_1_1(item)
        )
    return out
