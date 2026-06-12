"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringAlertSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_alert_summary

MonitoringAlertSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.monitoring_alert_summary.MonitoringAlertSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringAlertSummaryList) -> list:
    import aws_sdk_sagemaker.types.monitoring_alert_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.monitoring_alert_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MonitoringAlertSummaryList:
    import aws_sdk_sagemaker.types.monitoring_alert_summary

    out: MonitoringAlertSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.monitoring_alert_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
