"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMonitoringAlertRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_alert_name
    import aws_sdk_sagemaker.types.monitoring_datapoints_to_alert
    import aws_sdk_sagemaker.types.monitoring_evaluation_period
    import aws_sdk_sagemaker.types.monitoring_schedule_name


class UpdateMonitoringAlertRequest(TypedDict):
    monitoring_schedule_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of a monitoring schedule.</p>"""
    monitoring_alert_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_alert_name.MonitoringAlertName"
    ]
    """<p>The name of a monitoring alert.</p>"""
    datapoints_to_alert: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_datapoints_to_alert.MonitoringDatapointsToAlert"
    ]
    """<p>Within <code>EvaluationPeriod</code>, how many execution failures will raise an alert.</p>"""
    evaluation_period: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_evaluation_period.MonitoringEvaluationPeriod"
    ]
    """<p>The number of most recent monitoring executions to consider when evaluating alert status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMonitoringAlertRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_alert_name" in value:
        out["MonitoringAlertName"] = value["monitoring_alert_name"]
    if "datapoints_to_alert" in value:
        out["DatapointsToAlert"] = value["datapoints_to_alert"]
    if "evaluation_period" in value:
        out["EvaluationPeriod"] = value["evaluation_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMonitoringAlertRequest:
    out: UpdateMonitoringAlertRequest = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if "MonitoringAlertName" in data:
        out["monitoring_alert_name"] = data["MonitoringAlertName"]
    if "DatapointsToAlert" in data:
        out["datapoints_to_alert"] = data["DatapointsToAlert"]
    if "EvaluationPeriod" in data:
        out["evaluation_period"] = data["EvaluationPeriod"]
    return out
