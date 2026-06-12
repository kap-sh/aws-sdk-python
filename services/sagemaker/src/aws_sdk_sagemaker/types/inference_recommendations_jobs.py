"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRecommendationsJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_recommendations_job

InferenceRecommendationsJobs: TypeAlias = list[
    "aws_sdk_sagemaker.types.inference_recommendations_job.InferenceRecommendationsJob"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRecommendationsJobs) -> list:
    import aws_sdk_sagemaker.types.inference_recommendations_job

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.inference_recommendations_job.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceRecommendationsJobs:
    import aws_sdk_sagemaker.types.inference_recommendations_job

    out: InferenceRecommendationsJobs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.inference_recommendations_job.deserialize_aws_json_1_1(
                item
            )
        )
    return out
