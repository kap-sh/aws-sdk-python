"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringScheduleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_job_definition
    import aws_sdk_sagemaker.types.monitoring_job_definition_name
    import aws_sdk_sagemaker.types.monitoring_type
    import aws_sdk_sagemaker.types.schedule_config


class MonitoringScheduleConfig(TypedDict, closed=True):
    schedule_config: NotRequired[
        "aws_sdk_sagemaker.types.schedule_config.ScheduleConfig"
    ]
    """<p>Configures the monitoring schedule.</p>"""
    monitoring_job_definition: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition.MonitoringJobDefinition"
    ]
    """<p>Defines the monitoring job.</p>"""
    monitoring_job_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p>The name of the monitoring job definition to schedule.</p>"""
    monitoring_type: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_type.MonitoringType"
    ]
    """<p>The type of the monitoring job definition to schedule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringScheduleConfig) -> dict:
    out: dict = {}
    if "schedule_config" in value:
        import aws_sdk_sagemaker.types.schedule_config

        out["ScheduleConfig"] = (
            aws_sdk_sagemaker.types.schedule_config.serialize_aws_json_1_1(
                value["schedule_config"]
            )
        )
    if "monitoring_job_definition" in value:
        import aws_sdk_sagemaker.types.monitoring_job_definition

        out["MonitoringJobDefinition"] = (
            aws_sdk_sagemaker.types.monitoring_job_definition.serialize_aws_json_1_1(
                value["monitoring_job_definition"]
            )
        )
    if "monitoring_job_definition_name" in value:
        out["MonitoringJobDefinitionName"] = value["monitoring_job_definition_name"]
    if "monitoring_type" in value:
        import aws_sdk_sagemaker.types.monitoring_type

        out["MonitoringType"] = (
            aws_sdk_sagemaker.types.monitoring_type.serialize_aws_json_1_1(
                value["monitoring_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringScheduleConfig:
    out: MonitoringScheduleConfig = {}  # type: ignore[typeddict-item]
    if "ScheduleConfig" in data:
        import aws_sdk_sagemaker.types.schedule_config

        out["schedule_config"] = (
            aws_sdk_sagemaker.types.schedule_config.deserialize_aws_json_1_1(
                data["ScheduleConfig"]
            )
        )
    if "MonitoringJobDefinition" in data:
        import aws_sdk_sagemaker.types.monitoring_job_definition

        out["monitoring_job_definition"] = (
            aws_sdk_sagemaker.types.monitoring_job_definition.deserialize_aws_json_1_1(
                data["MonitoringJobDefinition"]
            )
        )
    if "MonitoringJobDefinitionName" in data:
        out["monitoring_job_definition_name"] = data["MonitoringJobDefinitionName"]
    if "MonitoringType" in data:
        import aws_sdk_sagemaker.types.monitoring_type

        out["monitoring_type"] = (
            aws_sdk_sagemaker.types.monitoring_type.deserialize_aws_json_1_1(
                data["MonitoringType"]
            )
        )
    return out
