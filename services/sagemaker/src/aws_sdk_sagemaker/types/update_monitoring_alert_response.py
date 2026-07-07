"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMonitoringAlertResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_alert_name
    import aws_sdk_sagemaker.types.monitoring_schedule_arn


class UpdateMonitoringAlertResponse(TypedDict, closed=True):
    monitoring_schedule_arn: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_arn.MonitoringScheduleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the monitoring schedule.</p>"""
    monitoring_alert_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_name.MonitoringAlertName"
    ]
    """<p>The name of a monitoring alert.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMonitoringAlertResponse) -> dict:
    out: dict = {}
    if "monitoring_schedule_arn" in value:
        out["MonitoringScheduleArn"] = value["monitoring_schedule_arn"]
    if "monitoring_alert_name" in value:
        out["MonitoringAlertName"] = value["monitoring_alert_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMonitoringAlertResponse:
    out: UpdateMonitoringAlertResponse = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleArn" in data:
        out["monitoring_schedule_arn"] = data["MonitoringScheduleArn"]
    if "MonitoringAlertName" in data:
        out["monitoring_alert_name"] = data["MonitoringAlertName"]
    return out
