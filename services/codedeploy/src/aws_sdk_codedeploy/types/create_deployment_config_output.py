"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_config_id


class CreateDeploymentConfigOutput(TypedDict, closed=True):
    deployment_config_id: NotRequired[
        "aws_sdk_codedeploy.types.deployment_config_id.DeploymentConfigId"
    ]
    """<p>A unique deployment configuration ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeploymentConfigOutput) -> dict:
    out: dict = {}
    if "deployment_config_id" in value:
        out["deploymentConfigId"] = value["deployment_config_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeploymentConfigOutput:
    out: CreateDeploymentConfigOutput = {}  # type: ignore[typeddict-item]
    if "deploymentConfigId" in data:
        out["deployment_config_id"] = data["deploymentConfigId"]
    return out
