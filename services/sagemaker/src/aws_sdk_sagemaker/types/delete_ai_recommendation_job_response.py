"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAIRecommendationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_job_arn


class DeleteAIRecommendationJobResponse(TypedDict, closed=True):
    ai_recommendation_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_job_arn.AIRecommendationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted recommendation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAIRecommendationJobResponse) -> dict:
    out: dict = {}
    if "ai_recommendation_job_arn" in value:
        out["AIRecommendationJobArn"] = value["ai_recommendation_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAIRecommendationJobResponse:
    out: DeleteAIRecommendationJobResponse = {}  # type: ignore[typeddict-item]
    if "AIRecommendationJobArn" in data:
        out["ai_recommendation_job_arn"] = data["AIRecommendationJobArn"]
    return out
