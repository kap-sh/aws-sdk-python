"""Generated from Smithy shape ``com.amazonaws.pi#CreatePerformanceAnalysisReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pi.types.analysis_report_id


class CreatePerformanceAnalysisReportResponse(TypedDict):
    analysis_report_id: NotRequired[
        "aws_sdk_pi.types.analysis_report_id.AnalysisReportId"
    ]
    """<p>A unique identifier for the created analysis report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePerformanceAnalysisReportResponse) -> dict:
    out: dict = {}
    if "analysis_report_id" in value:
        out["AnalysisReportId"] = value["analysis_report_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePerformanceAnalysisReportResponse:
    out: CreatePerformanceAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisReportId" in data:
        out["analysis_report_id"] = data["AnalysisReportId"]
    return out
