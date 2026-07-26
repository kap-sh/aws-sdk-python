"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_schedule

MonitoringScheduleList: TypeAlias = list[
    "capo_sagemaker.types.monitoring_schedule.MonitoringSchedule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringScheduleList) -> list:
    import capo_sagemaker.types.monitoring_schedule

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.monitoring_schedule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MonitoringScheduleList:
    import capo_sagemaker.types.monitoring_schedule

    out: MonitoringScheduleList = []
    for item in data:
        out.append(
            capo_sagemaker.types.monitoring_schedule.deserialize_aws_json_1_1(item)
        )
    return out
