"""Generated from Smithy shape ``com.amazonaws.costexplorer#StartSavingsPlansPurchaseRecommendationGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.recommendation_id
    import aws_sdk_cost_explorer.types.zoned_date_time


class StartSavingsPlansPurchaseRecommendationGenerationResponse(TypedDict, closed=True):
    recommendation_id: NotRequired[
        "aws_sdk_cost_explorer.types.recommendation_id.RecommendationId"
    ]
    """<p>The ID for this specific recommendation.</p>"""
    generation_started_time: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The start time of the recommendation generation.</p>"""
    estimated_completion_time: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The estimated time for when the recommendation generation will complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: StartSavingsPlansPurchaseRecommendationGenerationResponse,
) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "generation_started_time" in value:
        out["GenerationStartedTime"] = value["generation_started_time"]
    if "estimated_completion_time" in value:
        out["EstimatedCompletionTime"] = value["estimated_completion_time"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> StartSavingsPlansPurchaseRecommendationGenerationResponse:
    out: StartSavingsPlansPurchaseRecommendationGenerationResponse = {}  # type: ignore[typeddict-item]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "GenerationStartedTime" in data:
        out["generation_started_time"] = data["GenerationStartedTime"]
    if "EstimatedCompletionTime" in data:
        out["estimated_completion_time"] = data["EstimatedCompletionTime"]
    return out
