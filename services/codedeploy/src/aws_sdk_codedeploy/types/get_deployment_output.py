"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_info


class GetDeploymentOutput(TypedDict):
    deployment_info: NotRequired[
        "aws_sdk_codedeploy.types.deployment_info.DeploymentInfo"
    ]
    """<p>Information about the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment_info" in value:
        import aws_sdk_codedeploy.types.deployment_info

        out["deploymentInfo"] = (
            aws_sdk_codedeploy.types.deployment_info.serialize_aws_json_1_1(
                value["deployment_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentOutput:
    out: GetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "deploymentInfo" in data:
        import aws_sdk_codedeploy.types.deployment_info

        out["deployment_info"] = (
            aws_sdk_codedeploy.types.deployment_info.deserialize_aws_json_1_1(
                data["deploymentInfo"]
            )
        )
    return out
