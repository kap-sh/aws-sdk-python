"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.analysis_id
    import capo_cost_explorer.types.analysis_status
    import capo_cost_explorer.types.commitment_purchase_analysis_configuration
    import capo_cost_explorer.types.error_code
    import capo_cost_explorer.types.zoned_date_time


class AnalysisSummary(TypedDict, closed=True):
    estimated_completion_time: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The estimated time for when the analysis will complete.</p>"""
    analysis_completion_time: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The completion time of the analysis.</p>"""
    analysis_started_time: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The start time of the analysis.</p>"""
    analysis_status: NotRequired[
        "capo_cost_explorer.types.analysis_status.AnalysisStatus"
    ]
    """<p>The status of the analysis.</p>"""
    error_code: NotRequired["capo_cost_explorer.types.error_code.ErrorCode"]
    """<p>The error code used for the analysis.</p>"""
    analysis_id: NotRequired["capo_cost_explorer.types.analysis_id.AnalysisId"]
    """<p>The analysis ID that's associated with the commitment purchase analysis.</p>"""
    commitment_purchase_analysis_configuration: NotRequired[
        "capo_cost_explorer.types.commitment_purchase_analysis_configuration.CommitmentPurchaseAnalysisConfiguration"
    ]
    """<p>The configuration for the commitment purchase analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisSummary) -> dict:
    out: dict = {}
    if "estimated_completion_time" in value:
        out["EstimatedCompletionTime"] = value["estimated_completion_time"]
    if "analysis_completion_time" in value:
        out["AnalysisCompletionTime"] = value["analysis_completion_time"]
    if "analysis_started_time" in value:
        out["AnalysisStartedTime"] = value["analysis_started_time"]
    if "analysis_status" in value:
        import capo_cost_explorer.types.analysis_status

        out["AnalysisStatus"] = (
            capo_cost_explorer.types.analysis_status.serialize_aws_json_1_1(
                value["analysis_status"]
            )
        )
    if "error_code" in value:
        import capo_cost_explorer.types.error_code

        out["ErrorCode"] = capo_cost_explorer.types.error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "commitment_purchase_analysis_configuration" in value:
        import capo_cost_explorer.types.commitment_purchase_analysis_configuration

        out["CommitmentPurchaseAnalysisConfiguration"] = (
            capo_cost_explorer.types.commitment_purchase_analysis_configuration.serialize_aws_json_1_1(
                value["commitment_purchase_analysis_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisSummary:
    out: AnalysisSummary = {}  # type: ignore[typeddict-item]
    if "EstimatedCompletionTime" in data:
        out["estimated_completion_time"] = data["EstimatedCompletionTime"]
    if "AnalysisCompletionTime" in data:
        out["analysis_completion_time"] = data["AnalysisCompletionTime"]
    if "AnalysisStartedTime" in data:
        out["analysis_started_time"] = data["AnalysisStartedTime"]
    if "AnalysisStatus" in data:
        import capo_cost_explorer.types.analysis_status

        out["analysis_status"] = (
            capo_cost_explorer.types.analysis_status.deserialize_aws_json_1_1(
                data["AnalysisStatus"]
            )
        )
    if "ErrorCode" in data:
        import capo_cost_explorer.types.error_code

        out["error_code"] = (
            capo_cost_explorer.types.error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "CommitmentPurchaseAnalysisConfiguration" in data:
        import capo_cost_explorer.types.commitment_purchase_analysis_configuration

        out["commitment_purchase_analysis_configuration"] = (
            capo_cost_explorer.types.commitment_purchase_analysis_configuration.deserialize_aws_json_1_1(
                data["CommitmentPurchaseAnalysisConfiguration"]
            )
        )
    return out
