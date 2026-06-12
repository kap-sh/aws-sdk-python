"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StartAnalysisReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.analysis_report_id


class StartAnalysisReportResponse(TypedDict):
    analysis_report_id: (
        "aws_sdk_network_firewall.types.analysis_report_id.AnalysisReportId"
    )
    """<p>The unique ID of the query that ran when you requested an analysis report. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAnalysisReportResponse) -> dict:
    out: dict = {}
    out["AnalysisReportId"] = value["analysis_report_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAnalysisReportResponse:
    out: StartAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisReportId" in data:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        raise DeserializationError(
            "StartAnalysisReportResponse.analysis_report_id required"
        )
    return out
