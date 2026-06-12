"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_group_id


class CreateDeploymentGroupOutput(TypedDict):
    deployment_group_id: NotRequired[
        "aws_sdk_codedeploy.types.deployment_group_id.DeploymentGroupId"
    ]
    """<p>A unique deployment group ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeploymentGroupOutput) -> dict:
    out: dict = {}
    if "deployment_group_id" in value:
        out["deploymentGroupId"] = value["deployment_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeploymentGroupOutput:
    out: CreateDeploymentGroupOutput = {}  # type: ignore[typeddict-item]
    if "deploymentGroupId" in data:
        out["deployment_group_id"] = data["deploymentGroupId"]
    return out
