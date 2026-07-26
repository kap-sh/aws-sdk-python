"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_filter

TrainingPlanFilters: TypeAlias = list[
    "capo_sagemaker.types.training_plan_filter.TrainingPlanFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanFilters) -> list:
    import capo_sagemaker.types.training_plan_filter

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_plan_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingPlanFilters:
    import capo_sagemaker.types.training_plan_filter

    out: TrainingPlanFilters = []
    for item in data:
        out.append(
            capo_sagemaker.types.training_plan_filter.deserialize_aws_json_1_1(item)
        )
    return out
