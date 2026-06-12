"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateInferenceRecommendationsJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_arn


class CreateInferenceRecommendationsJobResponse(TypedDict):
    job_arn: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_arn.RecommendationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the recommendation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInferenceRecommendationsJobResponse) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInferenceRecommendationsJobResponse:
    out: CreateInferenceRecommendationsJobResponse = {}  # type: ignore[typeddict-item]
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    return out
