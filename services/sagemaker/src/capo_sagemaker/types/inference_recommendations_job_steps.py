"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRecommendationsJobSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_recommendations_job_step

InferenceRecommendationsJobSteps: TypeAlias = list[
    "capo_sagemaker.types.inference_recommendations_job_step.InferenceRecommendationsJobStep"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRecommendationsJobSteps) -> list:
    import capo_sagemaker.types.inference_recommendations_job_step

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.inference_recommendations_job_step.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceRecommendationsJobSteps:
    import capo_sagemaker.types.inference_recommendations_job_step

    out: InferenceRecommendationsJobSteps = []
    for item in data:
        out.append(
            capo_sagemaker.types.inference_recommendations_job_step.deserialize_aws_json_1_1(
                item
            )
        )
    return out
