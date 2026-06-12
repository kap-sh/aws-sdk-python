"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteDeploymentGroupInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.deployment_group_name


class DeleteDeploymentGroupInput(TypedDict):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""
    deployment_group_name: (
        "aws_sdk_codedeploy.types.deployment_group_name.DeploymentGroupName"
    )
    """<p>The name of a deployment group for the specified application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeploymentGroupInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    out["deploymentGroupName"] = value["deployment_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeploymentGroupInput:
    out: DeleteDeploymentGroupInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "DeleteDeploymentGroupInput.application_name required"
        )
    if "deploymentGroupName" in data:
        out["deployment_group_name"] = data["deploymentGroupName"]
    else:
        raise DeserializationError(
            "DeleteDeploymentGroupInput.deployment_group_name required"
        )
    return out
