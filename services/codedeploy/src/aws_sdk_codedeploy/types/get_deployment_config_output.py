"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_config_info


class GetDeploymentConfigOutput(TypedDict):
    deployment_config_info: NotRequired[
        "aws_sdk_codedeploy.types.deployment_config_info.DeploymentConfigInfo"
    ]
    """<p>Information about the deployment configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentConfigOutput) -> dict:
    out: dict = {}
    if "deployment_config_info" in value:
        import aws_sdk_codedeploy.types.deployment_config_info

        out["deploymentConfigInfo"] = (
            aws_sdk_codedeploy.types.deployment_config_info.serialize_aws_json_1_1(
                value["deployment_config_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentConfigOutput:
    out: GetDeploymentConfigOutput = {}  # type: ignore[typeddict-item]
    if "deploymentConfigInfo" in data:
        import aws_sdk_codedeploy.types.deployment_config_info

        out["deployment_config_info"] = (
            aws_sdk_codedeploy.types.deployment_config_info.deserialize_aws_json_1_1(
                data["deploymentConfigInfo"]
            )
        )
    return out
