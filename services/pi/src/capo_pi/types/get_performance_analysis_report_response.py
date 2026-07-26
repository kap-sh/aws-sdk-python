"""Generated from Smithy shape ``com.amazonaws.pi#GetPerformanceAnalysisReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.analysis_report


class GetPerformanceAnalysisReportResponse(TypedDict, closed=True):
    analysis_report: NotRequired["capo_pi.types.analysis_report.AnalysisReport"]
    """<p>The summary of the performance analysis report created for a time period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPerformanceAnalysisReportResponse) -> dict:
    out: dict = {}
    if "analysis_report" in value:
        import capo_pi.types.analysis_report

        out["AnalysisReport"] = capo_pi.types.analysis_report.serialize_aws_json_1_1(
            value["analysis_report"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPerformanceAnalysisReportResponse:
    out: GetPerformanceAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisReport" in data:
        import capo_pi.types.analysis_report

        out["analysis_report"] = capo_pi.types.analysis_report.deserialize_aws_json_1_1(
            data["AnalysisReport"]
        )
    return out
