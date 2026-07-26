"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAIRecommendationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_entity_name


class DescribeAIRecommendationJobRequest(TypedDict, closed=True):
    ai_recommendation_job_name: NotRequired[
        "capo_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI recommendation job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAIRecommendationJobRequest) -> dict:
    out: dict = {}
    if "ai_recommendation_job_name" in value:
        out["AIRecommendationJobName"] = value["ai_recommendation_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAIRecommendationJobRequest:
    out: DescribeAIRecommendationJobRequest = {}  # type: ignore[typeddict-item]
    if "AIRecommendationJobName" in data:
        out["ai_recommendation_job_name"] = data["AIRecommendationJobName"]
    return out
