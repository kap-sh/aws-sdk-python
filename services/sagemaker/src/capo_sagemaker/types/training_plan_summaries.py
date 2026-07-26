"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_summary

TrainingPlanSummaries: TypeAlias = list[
    "capo_sagemaker.types.training_plan_summary.TrainingPlanSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanSummaries) -> list:
    import capo_sagemaker.types.training_plan_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_plan_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingPlanSummaries:
    import capo_sagemaker.types.training_plan_summary

    out: TrainingPlanSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.training_plan_summary.deserialize_aws_json_1_1(item)
        )
    return out
