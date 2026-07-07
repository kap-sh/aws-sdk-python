"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StartRecommendationReportGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.recommendation_task_id


class StartRecommendationReportGenerationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_migrationhubstrategy.types.recommendation_task_id.RecommendationTaskId"
    ]
    """<p> The ID of the recommendation report generation task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecommendationReportGenerationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> StartRecommendationReportGenerationResponse:
    out: StartRecommendationReportGenerationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
