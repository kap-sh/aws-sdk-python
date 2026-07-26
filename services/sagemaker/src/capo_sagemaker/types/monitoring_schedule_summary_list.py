"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringScheduleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_schedule_summary

MonitoringScheduleSummaryList: TypeAlias = list[
    "capo_sagemaker.types.monitoring_schedule_summary.MonitoringScheduleSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringScheduleSummaryList) -> list:
    import capo_sagemaker.types.monitoring_schedule_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.monitoring_schedule_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MonitoringScheduleSummaryList:
    import capo_sagemaker.types.monitoring_schedule_summary

    out: MonitoringScheduleSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.monitoring_schedule_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
