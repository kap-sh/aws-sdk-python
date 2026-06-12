"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_alert_history_summary

MonitoringAlertHistoryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.monitoring_alert_history_summary.MonitoringAlertHistorySummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertHistoryList) -> list:
    import aws_sdk_sagemaker.types.monitoring_alert_history_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.monitoring_alert_history_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MonitoringAlertHistoryList:
    import aws_sdk_sagemaker.types.monitoring_alert_history_summary

    out: MonitoringAlertHistoryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.monitoring_alert_history_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
