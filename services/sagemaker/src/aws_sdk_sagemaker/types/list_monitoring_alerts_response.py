"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMonitoringAlertsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_alert_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListMonitoringAlertsResponse(TypedDict):
    monitoring_alert_summaries: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_summary_list.MonitoringAlertSummaryList"
    ]
    """<p>A JSON array where each element is a summary for a monitoring alert.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of alerts, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitoringAlertsResponse) -> dict:
    out: dict = {}
    if "monitoring_alert_summaries" in value:
        import aws_sdk_sagemaker.types.monitoring_alert_summary_list

        out["MonitoringAlertSummaries"] = (
            aws_sdk_sagemaker.types.monitoring_alert_summary_list.serialize_aws_json_1_1(
                value["monitoring_alert_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitoringAlertsResponse:
    out: ListMonitoringAlertsResponse = {}  # type: ignore[typeddict-item]
    if "MonitoringAlertSummaries" in data:
        import aws_sdk_sagemaker.types.monitoring_alert_summary_list

        out["monitoring_alert_summaries"] = (
            aws_sdk_sagemaker.types.monitoring_alert_summary_list.deserialize_aws_json_1_1(
                data["MonitoringAlertSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
