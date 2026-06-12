"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_rollback_alarms
    import aws_sdk_sagemaker.types.rolling_deployment_policy
    import aws_sdk_sagemaker.types.wait_time_interval_in_seconds


class DeploymentConfiguration(TypedDict):
    rolling_update_policy: NotRequired[
        "aws_sdk_sagemaker.types.rolling_deployment_policy.RollingDeploymentPolicy"
    ]
    """<p>The policy that SageMaker uses when updating the AMI versions of the cluster. </p>"""
    wait_interval_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.wait_time_interval_in_seconds.WaitTimeIntervalInSeconds"
    ]
    """<p>The duration in seconds that SageMaker waits before updating more instances in the cluster.</p>"""
    auto_rollback_configuration: NotRequired[
        "aws_sdk_sagemaker.types.auto_rollback_alarms.AutoRollbackAlarms"
    ]
    """<p>An array that contains the alarms that SageMaker monitors to know whether to roll back the AMI update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentConfiguration) -> dict:
    out: dict = {}
    if "rolling_update_policy" in value:
        import aws_sdk_sagemaker.types.rolling_deployment_policy

        out["RollingUpdatePolicy"] = (
            aws_sdk_sagemaker.types.rolling_deployment_policy.serialize_aws_json_1_1(
                value["rolling_update_policy"]
            )
        )
    if "wait_interval_in_seconds" in value:
        out["WaitIntervalInSeconds"] = value["wait_interval_in_seconds"]
    if "auto_rollback_configuration" in value:
        import aws_sdk_sagemaker.types.auto_rollback_alarms

        out["AutoRollbackConfiguration"] = (
            aws_sdk_sagemaker.types.auto_rollback_alarms.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentConfiguration:
    out: DeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if "RollingUpdatePolicy" in data:
        import aws_sdk_sagemaker.types.rolling_deployment_policy

        out["rolling_update_policy"] = (
            aws_sdk_sagemaker.types.rolling_deployment_policy.deserialize_aws_json_1_1(
                data["RollingUpdatePolicy"]
            )
        )
    if "WaitIntervalInSeconds" in data:
        out["wait_interval_in_seconds"] = data["WaitIntervalInSeconds"]
    if "AutoRollbackConfiguration" in data:
        import aws_sdk_sagemaker.types.auto_rollback_alarms

        out["auto_rollback_configuration"] = (
            aws_sdk_sagemaker.types.auto_rollback_alarms.deserialize_aws_json_1_1(
                data["AutoRollbackConfiguration"]
            )
        )
    return out
