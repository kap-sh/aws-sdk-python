"""Generated from Smithy shape ``com.amazonaws.pi#ListPerformanceAnalysisReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pi.types.analysis_report_summary_list
    import aws_sdk_pi.types.next_token


class ListPerformanceAnalysisReportsResponse(TypedDict, closed=True):
    analysis_reports: NotRequired[
        "aws_sdk_pi.types.analysis_report_summary_list.AnalysisReportSummaryList"
    ]
    """<p>List of reports including the report identifier, start and end time, creation time, and status.</p>"""
    next_token: NotRequired["aws_sdk_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPerformanceAnalysisReportsResponse) -> dict:
    out: dict = {}
    if "analysis_reports" in value:
        import aws_sdk_pi.types.analysis_report_summary_list

        out["AnalysisReports"] = (
            aws_sdk_pi.types.analysis_report_summary_list.serialize_aws_json_1_1(
                value["analysis_reports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPerformanceAnalysisReportsResponse:
    out: ListPerformanceAnalysisReportsResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisReports" in data:
        import aws_sdk_pi.types.analysis_report_summary_list

        out["analysis_reports"] = (
            aws_sdk_pi.types.analysis_report_summary_list.deserialize_aws_json_1_1(
                data["AnalysisReports"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
