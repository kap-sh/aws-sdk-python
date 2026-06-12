"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetRecommendationReportDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.recommendation_task_id


class GetRecommendationReportDetailsRequest(TypedDict):
    id: "aws_sdk_migrationhubstrategy.types.recommendation_task_id.RecommendationTaskId"
    """<p> The recommendation report generation task <code>id</code> returned by <a>StartRecommendationReportGeneration</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationReportDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendationReportDetailsRequest:
    out: GetRecommendationReportDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
