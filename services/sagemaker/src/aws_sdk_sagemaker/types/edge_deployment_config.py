"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeDeploymentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_handling_policy


class EdgeDeploymentConfig(TypedDict, closed=True):
    failure_handling_policy: NotRequired[
        "aws_sdk_sagemaker.types.failure_handling_policy.FailureHandlingPolicy"
    ]
    """<p>Toggle that determines whether to rollback to previous configuration if the current deployment fails. By default this is turned on. You may turn this off if you want to investigate the errors yourself.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeDeploymentConfig) -> dict:
    out: dict = {}
    if "failure_handling_policy" in value:
        import aws_sdk_sagemaker.types.failure_handling_policy

        out["FailureHandlingPolicy"] = (
            aws_sdk_sagemaker.types.failure_handling_policy.serialize_aws_json_1_1(
                value["failure_handling_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeDeploymentConfig:
    out: EdgeDeploymentConfig = {}  # type: ignore[typeddict-item]
    if "FailureHandlingPolicy" in data:
        import aws_sdk_sagemaker.types.failure_handling_policy

        out["failure_handling_policy"] = (
            aws_sdk_sagemaker.types.failure_handling_policy.deserialize_aws_json_1_1(
                data["FailureHandlingPolicy"]
            )
        )
    return out
