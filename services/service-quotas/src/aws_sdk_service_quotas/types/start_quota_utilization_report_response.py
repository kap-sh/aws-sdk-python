"""Generated from Smithy shape ``com.amazonaws.servicequotas#StartQuotaUtilizationReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.report_id
    import aws_sdk_service_quotas.types.report_message
    import aws_sdk_service_quotas.types.report_status


class StartQuotaUtilizationReportResponse(TypedDict):
    report_id: NotRequired["aws_sdk_service_quotas.types.report_id.ReportId"]
    """<p>A unique identifier for the quota utilization report. Use this identifier with the <code>GetQuotaUtilizationReport</code> operation to retrieve the report results.</p>"""
    status: NotRequired["aws_sdk_service_quotas.types.report_status.ReportStatus"]
    """<p>The current status of the report generation. The status will be <code>PENDING</code> when the report is first initiated.</p>"""
    message: NotRequired["aws_sdk_service_quotas.types.report_message.ReportMessage"]
    """<p>An optional message providing additional information about the report generation status. This field may contain details about the report initiation or indicate if an existing recent report is being reused.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQuotaUtilizationReportResponse) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["ReportId"] = value["report_id"]
    if "status" in value:
        import aws_sdk_service_quotas.types.report_status

        out["Status"] = (
            aws_sdk_service_quotas.types.report_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQuotaUtilizationReportResponse:
    out: StartQuotaUtilizationReportResponse = {}  # type: ignore[typeddict-item]
    if "ReportId" in data:
        out["report_id"] = data["ReportId"]
    if "Status" in data:
        import aws_sdk_service_quotas.types.report_status

        out["status"] = (
            aws_sdk_service_quotas.types.report_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
