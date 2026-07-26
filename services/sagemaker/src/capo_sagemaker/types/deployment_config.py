"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_rollback_config
    import capo_sagemaker.types.blue_green_update_policy
    import capo_sagemaker.types.rolling_update_policy


class DeploymentConfig(TypedDict, closed=True):
    blue_green_update_policy: NotRequired[
        "capo_sagemaker.types.blue_green_update_policy.BlueGreenUpdatePolicy"
    ]
    """<p>Update policy for a blue/green deployment. If this update policy is specified, SageMaker creates a new fleet during the deployment while maintaining the old fleet. SageMaker flips traffic to the new fleet according to the specified traffic routing configuration. Only one update policy should be used in the deployment configuration. If no update policy is specified, SageMaker uses a blue/green deployment strategy with all at once traffic shifting by default.</p>"""
    rolling_update_policy: NotRequired[
        "capo_sagemaker.types.rolling_update_policy.RollingUpdatePolicy"
    ]
    """<p>Specifies a rolling deployment strategy for updating a SageMaker endpoint.</p>"""
    auto_rollback_configuration: NotRequired[
        "capo_sagemaker.types.auto_rollback_config.AutoRollbackConfig"
    ]
    """<p>Automatic rollback configuration for handling endpoint deployment failures and recovery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentConfig) -> dict:
    out: dict = {}
    if "blue_green_update_policy" in value:
        import capo_sagemaker.types.blue_green_update_policy

        out["BlueGreenUpdatePolicy"] = (
            capo_sagemaker.types.blue_green_update_policy.serialize_aws_json_1_1(
                value["blue_green_update_policy"]
            )
        )
    if "rolling_update_policy" in value:
        import capo_sagemaker.types.rolling_update_policy

        out["RollingUpdatePolicy"] = (
            capo_sagemaker.types.rolling_update_policy.serialize_aws_json_1_1(
                value["rolling_update_policy"]
            )
        )
    if "auto_rollback_configuration" in value:
        import capo_sagemaker.types.auto_rollback_config

        out["AutoRollbackConfiguration"] = (
            capo_sagemaker.types.auto_rollback_config.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentConfig:
    out: DeploymentConfig = {}  # type: ignore[typeddict-item]
    if "BlueGreenUpdatePolicy" in data:
        import capo_sagemaker.types.blue_green_update_policy

        out["blue_green_update_policy"] = (
            capo_sagemaker.types.blue_green_update_policy.deserialize_aws_json_1_1(
                data["BlueGreenUpdatePolicy"]
            )
        )
    if "RollingUpdatePolicy" in data:
        import capo_sagemaker.types.rolling_update_policy

        out["rolling_update_policy"] = (
            capo_sagemaker.types.rolling_update_policy.deserialize_aws_json_1_1(
                data["RollingUpdatePolicy"]
            )
        )
    if "AutoRollbackConfiguration" in data:
        import capo_sagemaker.types.auto_rollback_config

        out["auto_rollback_configuration"] = (
            capo_sagemaker.types.auto_rollback_config.deserialize_aws_json_1_1(
                data["AutoRollbackConfiguration"]
            )
        )
    return out
