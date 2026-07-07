"""Generated from Smithy shape ``com.amazonaws.costexplorer#StartCommitmentPurchaseAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.analysis_id
    import aws_sdk_cost_explorer.types.zoned_date_time


class StartCommitmentPurchaseAnalysisResponse(TypedDict, closed=True):
    analysis_id: "aws_sdk_cost_explorer.types.analysis_id.AnalysisId"
    """<p>The analysis ID that's associated with the commitment purchase analysis.</p>"""
    analysis_started_time: "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    """<p>The start time of the analysis.</p>"""
    estimated_completion_time: (
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    )
    """<p>The estimated time for when the analysis will complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCommitmentPurchaseAnalysisResponse) -> dict:
    out: dict = {}
    out["AnalysisId"] = value["analysis_id"]
    out["AnalysisStartedTime"] = value["analysis_started_time"]
    out["EstimatedCompletionTime"] = value["estimated_completion_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCommitmentPurchaseAnalysisResponse:
    out: StartCommitmentPurchaseAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    else:
        raise DeserializationError(
            "StartCommitmentPurchaseAnalysisResponse.analysis_id required"
        )
    if "AnalysisStartedTime" in data:
        out["analysis_started_time"] = data["AnalysisStartedTime"]
    else:
        raise DeserializationError(
            "StartCommitmentPurchaseAnalysisResponse.analysis_started_time required"
        )
    if "EstimatedCompletionTime" in data:
        out["estimated_completion_time"] = data["EstimatedCompletionTime"]
    else:
        raise DeserializationError(
            "StartCommitmentPurchaseAnalysisResponse.estimated_completion_time required"
        )
    return out
