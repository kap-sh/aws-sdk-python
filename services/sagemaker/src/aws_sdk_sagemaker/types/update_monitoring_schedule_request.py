"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMonitoringScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_schedule_config
    import aws_sdk_sagemaker.types.monitoring_schedule_name


class UpdateMonitoringScheduleRequest(TypedDict):
    monitoring_schedule_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of the monitoring schedule. The name must be unique within an Amazon Web Services Region within an Amazon Web Services account.</p>"""
    monitoring_schedule_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_config.MonitoringScheduleConfig"
    ]
    """<p>The configuration object that specifies the monitoring schedule and defines the monitoring job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMonitoringScheduleRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_schedule_config" in value:
        import aws_sdk_sagemaker.types.monitoring_schedule_config

        out["MonitoringScheduleConfig"] = (
            aws_sdk_sagemaker.types.monitoring_schedule_config.serialize_aws_json_1_1(
                value["monitoring_schedule_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMonitoringScheduleRequest:
    out: UpdateMonitoringScheduleRequest = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if "MonitoringScheduleConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_schedule_config

        out["monitoring_schedule_config"] = (
            aws_sdk_sagemaker.types.monitoring_schedule_config.deserialize_aws_json_1_1(
                data["MonitoringScheduleConfig"]
            )
        )
    return out
