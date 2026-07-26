"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_alert_actions
    import capo_sagemaker.types.monitoring_alert_name
    import capo_sagemaker.types.monitoring_alert_status
    import capo_sagemaker.types.monitoring_datapoints_to_alert
    import capo_sagemaker.types.monitoring_evaluation_period
    import capo_sagemaker.types.timestamp


class MonitoringAlertSummary(TypedDict, closed=True):
    monitoring_alert_name: NotRequired[
        "capo_sagemaker.types.monitoring_alert_name.MonitoringAlertName"
    ]
    """<p>The name of a monitoring alert.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when a monitor alert was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when a monitor alert was last updated.</p>"""
    alert_status: NotRequired[
        "capo_sagemaker.types.monitoring_alert_status.MonitoringAlertStatus"
    ]
    """<p>The current status of an alert.</p>"""
    datapoints_to_alert: NotRequired[
        "capo_sagemaker.types.monitoring_datapoints_to_alert.MonitoringDatapointsToAlert"
    ]
    """<p>Within <code>EvaluationPeriod</code>, how many execution failures will raise an alert.</p>"""
    evaluation_period: NotRequired[
        "capo_sagemaker.types.monitoring_evaluation_period.MonitoringEvaluationPeriod"
    ]
    """<p>The number of most recent monitoring executions to consider when evaluating alert status.</p>"""
    actions: NotRequired[
        "capo_sagemaker.types.monitoring_alert_actions.MonitoringAlertActions"
    ]
    """<p>A list of alert actions taken in response to an alert going into <code>InAlert</code> status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertSummary) -> dict:
    out: dict = {}
    if "monitoring_alert_name" in value:
        out["MonitoringAlertName"] = value["monitoring_alert_name"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "alert_status" in value:
        import capo_sagemaker.types.monitoring_alert_status

        out["AlertStatus"] = (
            capo_sagemaker.types.monitoring_alert_status.serialize_aws_json_1_1(
                value["alert_status"]
            )
        )
    if "datapoints_to_alert" in value:
        out["DatapointsToAlert"] = value["datapoints_to_alert"]
    if "evaluation_period" in value:
        out["EvaluationPeriod"] = value["evaluation_period"]
    if "actions" in value:
        import capo_sagemaker.types.monitoring_alert_actions

        out["Actions"] = (
            capo_sagemaker.types.monitoring_alert_actions.serialize_aws_json_1_1(
                value["actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringAlertSummary:
    out: MonitoringAlertSummary = {}  # type: ignore[typeddict-item]
    if "MonitoringAlertName" in data:
        out["monitoring_alert_name"] = data["MonitoringAlertName"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "AlertStatus" in data:
        import capo_sagemaker.types.monitoring_alert_status

        out["alert_status"] = (
            capo_sagemaker.types.monitoring_alert_status.deserialize_aws_json_1_1(
                data["AlertStatus"]
            )
        )
    if "DatapointsToAlert" in data:
        out["datapoints_to_alert"] = data["DatapointsToAlert"]
    if "EvaluationPeriod" in data:
        out["evaluation_period"] = data["EvaluationPeriod"]
    if "Actions" in data:
        import capo_sagemaker.types.monitoring_alert_actions

        out["actions"] = (
            capo_sagemaker.types.monitoring_alert_actions.deserialize_aws_json_1_1(
                data["Actions"]
            )
        )
    return out
