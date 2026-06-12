"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_group_info_list
    import aws_sdk_codedeploy.types.error_message


class BatchGetDeploymentGroupsOutput(TypedDict):
    deployment_groups_info: NotRequired[
        "aws_sdk_codedeploy.types.deployment_group_info_list.DeploymentGroupInfoList"
    ]
    """<p>Information about the deployment groups.</p>"""
    error_message: NotRequired["aws_sdk_codedeploy.types.error_message.ErrorMessage"]
    """<p>Information about errors that might have occurred during the API call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentGroupsOutput) -> dict:
    out: dict = {}
    if "deployment_groups_info" in value:
        import aws_sdk_codedeploy.types.deployment_group_info_list

        out["deploymentGroupsInfo"] = (
            aws_sdk_codedeploy.types.deployment_group_info_list.serialize_aws_json_1_1(
                value["deployment_groups_info"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentGroupsOutput:
    out: BatchGetDeploymentGroupsOutput = {}  # type: ignore[typeddict-item]
    if "deploymentGroupsInfo" in data:
        import aws_sdk_codedeploy.types.deployment_group_info_list

        out["deployment_groups_info"] = (
            aws_sdk_codedeploy.types.deployment_group_info_list.deserialize_aws_json_1_1(
                data["deploymentGroupsInfo"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
