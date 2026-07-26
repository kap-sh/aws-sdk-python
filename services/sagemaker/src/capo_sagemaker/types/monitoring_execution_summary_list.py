"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_execution_summary

MonitoringExecutionSummaryList: TypeAlias = list[
    "capo_sagemaker.types.monitoring_execution_summary.MonitoringExecutionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringExecutionSummaryList) -> list:
    import capo_sagemaker.types.monitoring_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.monitoring_execution_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MonitoringExecutionSummaryList:
    import capo_sagemaker.types.monitoring_execution_summary

    out: MonitoringExecutionSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.monitoring_execution_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
