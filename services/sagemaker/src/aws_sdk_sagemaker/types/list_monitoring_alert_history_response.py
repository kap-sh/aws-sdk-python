"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMonitoringAlertHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_alert_history_list
    import aws_sdk_sagemaker.types.next_token


class ListMonitoringAlertHistoryResponse(TypedDict):
    monitoring_alert_history: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_history_list.MonitoringAlertHistoryList"
    ]
    """<p>An alert history for a model monitoring schedule.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of alerts, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitoringAlertHistoryResponse) -> dict:
    out: dict = {}
    if "monitoring_alert_history" in value:
        import aws_sdk_sagemaker.types.monitoring_alert_history_list

        out["MonitoringAlertHistory"] = (
            aws_sdk_sagemaker.types.monitoring_alert_history_list.serialize_aws_json_1_1(
                value["monitoring_alert_history"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitoringAlertHistoryResponse:
    out: ListMonitoringAlertHistoryResponse = {}  # type: ignore[typeddict-item]
    if "MonitoringAlertHistory" in data:
        import aws_sdk_sagemaker.types.monitoring_alert_history_list

        out["monitoring_alert_history"] = (
            aws_sdk_sagemaker.types.monitoring_alert_history_list.deserialize_aws_json_1_1(
                data["MonitoringAlertHistory"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
