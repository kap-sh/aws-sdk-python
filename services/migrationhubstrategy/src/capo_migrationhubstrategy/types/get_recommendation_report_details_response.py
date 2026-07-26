"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetRecommendationReportDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.recommendation_report_details
    import capo_migrationhubstrategy.types.recommendation_task_id


class GetRecommendationReportDetailsResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_task_id.RecommendationTaskId"
    ]
    """<p> The ID of the recommendation report generation task. See the response of <a>StartRecommendationReportGeneration</a>. </p>"""
    recommendation_report_details: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_report_details.RecommendationReportDetails"
    ]
    """<p> Detailed information about the recommendation report. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationReportDetailsResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "recommendation_report_details" in value:
        import capo_migrationhubstrategy.types.recommendation_report_details

        out["recommendationReportDetails"] = (
            capo_migrationhubstrategy.types.recommendation_report_details.serialize_json(
                value["recommendation_report_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationReportDetailsResponse:
    out: GetRecommendationReportDetailsResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "recommendationReportDetails" in data:
        import capo_migrationhubstrategy.types.recommendation_report_details

        out["recommendation_report_details"] = (
            capo_migrationhubstrategy.types.recommendation_report_details.deserialize_json(
                data["recommendationReportDetails"]
            )
        )
    return out
