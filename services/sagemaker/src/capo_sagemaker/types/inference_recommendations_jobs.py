"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRecommendationsJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_recommendations_job

InferenceRecommendationsJobs: TypeAlias = list[
    "capo_sagemaker.types.inference_recommendations_job.InferenceRecommendationsJob"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRecommendationsJobs) -> list:
    import capo_sagemaker.types.inference_recommendations_job

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.inference_recommendations_job.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceRecommendationsJobs:
    import capo_sagemaker.types.inference_recommendations_job

    out: InferenceRecommendationsJobs = []
    for item in data:
        out.append(
            capo_sagemaker.types.inference_recommendations_job.deserialize_aws_json_1_1(
                item
            )
        )
    return out
