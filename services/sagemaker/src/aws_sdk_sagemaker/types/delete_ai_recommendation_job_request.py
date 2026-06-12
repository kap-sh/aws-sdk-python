"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAIRecommendationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_entity_name


class DeleteAIRecommendationJobRequest(TypedDict):
    ai_recommendation_job_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI recommendation job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAIRecommendationJobRequest) -> dict:
    out: dict = {}
    if "ai_recommendation_job_name" in value:
        out["AIRecommendationJobName"] = value["ai_recommendation_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAIRecommendationJobRequest:
    out: DeleteAIRecommendationJobRequest = {}  # type: ignore[typeddict-item]
    if "AIRecommendationJobName" in data:
        out["ai_recommendation_job_name"] = data["AIRecommendationJobName"]
    return out
