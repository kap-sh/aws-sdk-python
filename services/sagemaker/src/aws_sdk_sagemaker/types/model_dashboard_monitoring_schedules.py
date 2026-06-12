"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardMonitoringSchedules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_dashboard_monitoring_schedule

ModelDashboardMonitoringSchedules: TypeAlias = list[
    "aws_sdk_sagemaker.types.model_dashboard_monitoring_schedule.ModelDashboardMonitoringSchedule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardMonitoringSchedules) -> list:
    import aws_sdk_sagemaker.types.model_dashboard_monitoring_schedule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.model_dashboard_monitoring_schedule.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ModelDashboardMonitoringSchedules:
    import aws_sdk_sagemaker.types.model_dashboard_monitoring_schedule

    out: ModelDashboardMonitoringSchedules = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.model_dashboard_monitoring_schedule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
