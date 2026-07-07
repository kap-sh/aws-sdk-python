"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_group_info


class GetDeploymentGroupOutput(TypedDict, closed=True):
    deployment_group_info: NotRequired[
        "aws_sdk_codedeploy.types.deployment_group_info.DeploymentGroupInfo"
    ]
    """<p>Information about the deployment group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentGroupOutput) -> dict:
    out: dict = {}
    if "deployment_group_info" in value:
        import aws_sdk_codedeploy.types.deployment_group_info

        out["deploymentGroupInfo"] = (
            aws_sdk_codedeploy.types.deployment_group_info.serialize_aws_json_1_1(
                value["deployment_group_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentGroupOutput:
    out: GetDeploymentGroupOutput = {}  # type: ignore[typeddict-item]
    if "deploymentGroupInfo" in data:
        import aws_sdk_codedeploy.types.deployment_group_info

        out["deployment_group_info"] = (
            aws_sdk_codedeploy.types.deployment_group_info.deserialize_aws_json_1_1(
                data["deploymentGroupInfo"]
            )
        )
    return out
