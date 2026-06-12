"""Generated from Smithy shape ``com.amazonaws.costexplorer#GenerationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generation_status
    import aws_sdk_cost_explorer.types.recommendation_id
    import aws_sdk_cost_explorer.types.zoned_date_time


class GenerationSummary(TypedDict):
    recommendation_id: NotRequired[
        "aws_sdk_cost_explorer.types.recommendation_id.RecommendationId"
    ]
    """<p>Indicates the ID for this specific recommendation.</p>"""
    generation_status: NotRequired[
        "aws_sdk_cost_explorer.types.generation_status.GenerationStatus"
    ]
    """<p>Indicates whether the recommendation generation succeeded, is processing, or failed.</p>"""
    generation_started_time: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>Indicates the start time of the recommendation generation.</p>"""
    generation_completion_time: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>Indicates the completion time of the recommendation generation.</p>"""
    estimated_completion_time: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>Indicates the estimated time for when the recommendation generation will complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerationSummary) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "generation_status" in value:
        import aws_sdk_cost_explorer.types.generation_status

        out["GenerationStatus"] = (
            aws_sdk_cost_explorer.types.generation_status.serialize_aws_json_1_1(
                value["generation_status"]
            )
        )
    if "generation_started_time" in value:
        out["GenerationStartedTime"] = value["generation_started_time"]
    if "generation_completion_time" in value:
        out["GenerationCompletionTime"] = value["generation_completion_time"]
    if "estimated_completion_time" in value:
        out["EstimatedCompletionTime"] = value["estimated_completion_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerationSummary:
    out: GenerationSummary = {}  # type: ignore[typeddict-item]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "GenerationStatus" in data:
        import aws_sdk_cost_explorer.types.generation_status

        out["generation_status"] = (
            aws_sdk_cost_explorer.types.generation_status.deserialize_aws_json_1_1(
                data["GenerationStatus"]
            )
        )
    if "GenerationStartedTime" in data:
        out["generation_started_time"] = data["GenerationStartedTime"]
    if "GenerationCompletionTime" in data:
        out["generation_completion_time"] = data["GenerationCompletionTime"]
    if "EstimatedCompletionTime" in data:
        out["estimated_completion_time"] = data["EstimatedCompletionTime"]
    return out
