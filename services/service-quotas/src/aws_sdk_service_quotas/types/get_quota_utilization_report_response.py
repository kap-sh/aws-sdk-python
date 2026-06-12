"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetQuotaUtilizationReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.date_time
    import aws_sdk_service_quotas.types.next_token
    import aws_sdk_service_quotas.types.quota_utilization_info_list
    import aws_sdk_service_quotas.types.report_error_code
    import aws_sdk_service_quotas.types.report_error_message
    import aws_sdk_service_quotas.types.report_id
    import aws_sdk_service_quotas.types.report_status
    import aws_sdk_service_quotas.types.total_count


class GetQuotaUtilizationReportResponse(TypedDict):
    report_id: NotRequired["aws_sdk_service_quotas.types.report_id.ReportId"]
    """<p>The unique identifier for the quota utilization report.</p>"""
    status: NotRequired["aws_sdk_service_quotas.types.report_status.ReportStatus"]
    """<p>The current status of the report generation. Possible values are:</p> <ul> <li> <p> <code>PENDING</code> - The report generation is in progress. Retry this operation after a few seconds.</p> </li> <li> <p> <code>IN_PROGRESS</code> - The report is being processed. Continue polling until the status changes to <code>COMPLETED</code>.</p> </li> <li> <p> <code>COMPLETED</code> - The report is ready and quota utilization data is available in the response.</p> </li> <li> <p> <code>FAILED</code> - The report generation failed. Check the <code>ErrorCode</code> and <code>ErrorMessage</code> fields for details.</p> </li> </ul>"""
    generated_at: NotRequired["aws_sdk_service_quotas.types.date_time.DateTime"]
    """<p>The timestamp when the report was generated, in ISO 8601 format.</p>"""
    total_count: NotRequired["aws_sdk_service_quotas.types.total_count.TotalCount"]
    """<p>The total number of quotas included in the report across all pages.</p>"""
    quotas: NotRequired[
        "aws_sdk_service_quotas.types.quota_utilization_info_list.QuotaUtilizationInfoList"
    ]
    """<p>A list of quota utilization records, sorted by utilization percentage in descending order. Each record includes the quota code, service code, service name, quota name, namespace, utilization percentage, default value, applied value, and whether the quota is adjustable. Up to 1,000 records are returned per page.</p>"""
    next_token: NotRequired["aws_sdk_service_quotas.types.next_token.NextToken"]
    """<p>A token that indicates more results are available. Include this token in the next request to retrieve the next page of results. If this field is not present, you have retrieved all available results.</p>"""
    error_code: NotRequired[
        "aws_sdk_service_quotas.types.report_error_code.ReportErrorCode"
    ]
    """<p>An error code indicating the reason for failure when the report status is <code>FAILED</code>. This field is only present when the status is <code>FAILED</code>.</p>"""
    error_message: NotRequired[
        "aws_sdk_service_quotas.types.report_error_message.ReportErrorMessage"
    ]
    """<p>A detailed error message describing the failure when the report status is <code>FAILED</code>. This field is only present when the status is <code>FAILED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQuotaUtilizationReportResponse) -> dict:
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
    if "generated_at" in value:
        import aws_sdk_service_quotas.types.date_time

        out["GeneratedAt"] = (
            aws_sdk_service_quotas.types.date_time.serialize_aws_json_1_1(
                value["generated_at"]
            )
        )
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    if "quotas" in value:
        import aws_sdk_service_quotas.types.quota_utilization_info_list

        out["Quotas"] = (
            aws_sdk_service_quotas.types.quota_utilization_info_list.serialize_aws_json_1_1(
                value["quotas"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQuotaUtilizationReportResponse:
    out: GetQuotaUtilizationReportResponse = {}  # type: ignore[typeddict-item]
    if "ReportId" in data:
        out["report_id"] = data["ReportId"]
    if "Status" in data:
        import aws_sdk_service_quotas.types.report_status

        out["status"] = (
            aws_sdk_service_quotas.types.report_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "GeneratedAt" in data:
        import aws_sdk_service_quotas.types.date_time

        out["generated_at"] = (
            aws_sdk_service_quotas.types.date_time.deserialize_aws_json_1_1(
                data["GeneratedAt"]
            )
        )
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    if "Quotas" in data:
        import aws_sdk_service_quotas.types.quota_utilization_info_list

        out["quotas"] = (
            aws_sdk_service_quotas.types.quota_utilization_info_list.deserialize_aws_json_1_1(
                data["Quotas"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
