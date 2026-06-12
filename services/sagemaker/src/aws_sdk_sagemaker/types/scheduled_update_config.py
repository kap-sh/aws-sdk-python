"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScheduledUpdateConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cron_schedule_expression
    import aws_sdk_sagemaker.types.deployment_configuration


class ScheduledUpdateConfig(TypedDict):
    schedule_expression: NotRequired[
        "aws_sdk_sagemaker.types.cron_schedule_expression.CronScheduleExpression"
    ]
    """<p>A cron expression that specifies the schedule that SageMaker follows when updating the AMI.</p>"""
    deployment_config: NotRequired[
        "aws_sdk_sagemaker.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>The configuration to use when updating the AMI versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledUpdateConfig) -> dict:
    out: dict = {}
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "deployment_config" in value:
        import aws_sdk_sagemaker.types.deployment_configuration

        out["DeploymentConfig"] = (
            aws_sdk_sagemaker.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledUpdateConfig:
    out: ScheduledUpdateConfig = {}  # type: ignore[typeddict-item]
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    if "DeploymentConfig" in data:
        import aws_sdk_sagemaker.types.deployment_configuration

        out["deployment_config"] = (
            aws_sdk_sagemaker.types.deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    return out
