"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRecommendationsJobSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_recommendations_job_step

InferenceRecommendationsJobSteps: TypeAlias = list[
    "aws_sdk_sagemaker.types.inference_recommendations_job_step.InferenceRecommendationsJobStep"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRecommendationsJobSteps) -> list:
    import aws_sdk_sagemaker.types.inference_recommendations_job_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.inference_recommendations_job_step.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceRecommendationsJobSteps:
    import aws_sdk_sagemaker.types.inference_recommendations_job_step

    out: InferenceRecommendationsJobSteps = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.inference_recommendations_job_step.deserialize_aws_json_1_1(
                item
            )
        )
    return out
