"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertHistorySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_alert_name
    import aws_sdk_sagemaker.types.monitoring_alert_status
    import aws_sdk_sagemaker.types.monitoring_schedule_name
    import aws_sdk_sagemaker.types.timestamp


class MonitoringAlertHistorySummary(TypedDict):
    monitoring_schedule_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of a monitoring schedule.</p>"""
    monitoring_alert_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_name.MonitoringAlertName"
    ]
    """<p>The name of a monitoring alert.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the first alert transition occurred in an alert history. An alert transition can be from status <code>InAlert</code> to <code>OK</code>, or from <code>OK</code> to <code>InAlert</code>.</p>"""
    alert_status: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_status.MonitoringAlertStatus"
    ]
    """<p>The current alert status of an alert.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertHistorySummary) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_alert_name" in value:
        out["MonitoringAlertName"] = value["monitoring_alert_name"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "alert_status" in value:
        import aws_sdk_sagemaker.types.monitoring_alert_status

        out["AlertStatus"] = (
            aws_sdk_sagemaker.types.monitoring_alert_status.serialize_aws_json_1_1(
                value["alert_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringAlertHistorySummary:
    out: MonitoringAlertHistorySummary = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if "MonitoringAlertName" in data:
        out["monitoring_alert_name"] = data["MonitoringAlertName"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "AlertStatus" in data:
        import aws_sdk_sagemaker.types.monitoring_alert_status

        out["alert_status"] = (
            aws_sdk_sagemaker.types.monitoring_alert_status.deserialize_aws_json_1_1(
                data["AlertStatus"]
            )
        )
    return out
