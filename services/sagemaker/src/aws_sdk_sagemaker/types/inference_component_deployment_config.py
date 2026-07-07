"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentDeploymentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_rollback_config
    import aws_sdk_sagemaker.types.inference_component_rolling_update_policy


class InferenceComponentDeploymentConfig(TypedDict, closed=True):
    rolling_update_policy: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_rolling_update_policy.InferenceComponentRollingUpdatePolicy"
    ]
    """<p>Specifies a rolling deployment strategy for updating a SageMaker AI endpoint.</p>"""
    auto_rollback_configuration: NotRequired[
        "aws_sdk_sagemaker.types.auto_rollback_config.AutoRollbackConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentDeploymentConfig) -> dict:
    out: dict = {}
    if "rolling_update_policy" in value:
        import aws_sdk_sagemaker.types.inference_component_rolling_update_policy

        out["RollingUpdatePolicy"] = (
            aws_sdk_sagemaker.types.inference_component_rolling_update_policy.serialize_aws_json_1_1(
                value["rolling_update_policy"]
            )
        )
    if "auto_rollback_configuration" in value:
        import aws_sdk_sagemaker.types.auto_rollback_config

        out["AutoRollbackConfiguration"] = (
            aws_sdk_sagemaker.types.auto_rollback_config.serialize_aws_json_1_1(
                value["auto_rollback_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentDeploymentConfig:
    out: InferenceComponentDeploymentConfig = {}  # type: ignore[typeddict-item]
    if "RollingUpdatePolicy" in data:
        import aws_sdk_sagemaker.types.inference_component_rolling_update_policy

        out["rolling_update_policy"] = (
            aws_sdk_sagemaker.types.inference_component_rolling_update_policy.deserialize_aws_json_1_1(
                data["RollingUpdatePolicy"]
            )
        )
    if "AutoRollbackConfiguration" in data:
        import aws_sdk_sagemaker.types.auto_rollback_config

        out["auto_rollback_configuration"] = (
            aws_sdk_sagemaker.types.auto_rollback_config.deserialize_aws_json_1_1(
                data["AutoRollbackConfiguration"]
            )
        )
    return out
