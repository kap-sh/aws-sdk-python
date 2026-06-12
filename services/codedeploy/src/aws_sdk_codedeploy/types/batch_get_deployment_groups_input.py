"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentGroupsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.deployment_groups_list


class BatchGetDeploymentGroupsInput(TypedDict):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the applicable user or Amazon Web Services account.</p>"""
    deployment_group_names: (
        "aws_sdk_codedeploy.types.deployment_groups_list.DeploymentGroupsList"
    )
    """<p>The names of the deployment groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentGroupsInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    import aws_sdk_codedeploy.types.deployment_groups_list

    out["deploymentGroupNames"] = (
        aws_sdk_codedeploy.types.deployment_groups_list.serialize_aws_json_1_1(
            value["deployment_group_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentGroupsInput:
    out: BatchGetDeploymentGroupsInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "BatchGetDeploymentGroupsInput.application_name required"
        )
    if "deploymentGroupNames" in data:
        import aws_sdk_codedeploy.types.deployment_groups_list

        out["deployment_group_names"] = (
            aws_sdk_codedeploy.types.deployment_groups_list.deserialize_aws_json_1_1(
                data["deploymentGroupNames"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDeploymentGroupsInput.deployment_group_names required"
        )
    return out
