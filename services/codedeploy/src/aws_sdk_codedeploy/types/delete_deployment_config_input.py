"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteDeploymentConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_config_name


class DeleteDeploymentConfigInput(TypedDict, closed=True):
    deployment_config_name: (
        "aws_sdk_codedeploy.types.deployment_config_name.DeploymentConfigName"
    )
    """<p>The name of a deployment configuration associated with the user or Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeploymentConfigInput) -> dict:
    out: dict = {}
    out["deploymentConfigName"] = value["deployment_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeploymentConfigInput:
    out: DeleteDeploymentConfigInput = {}  # type: ignore[typeddict-item]
    if "deploymentConfigName" in data:
        out["deployment_config_name"] = data["deploymentConfigName"]
    else:
        raise DeserializationError(
            "DeleteDeploymentConfigInput.deployment_config_name required"
        )
    return out
