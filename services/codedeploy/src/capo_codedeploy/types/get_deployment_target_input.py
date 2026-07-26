"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentTargetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.target_id


class GetDeploymentTargetInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment. </p>"""
    target_id: "capo_codedeploy.types.target_id.TargetId"
    """<p> The unique ID of a deployment target. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentTargetInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    out["targetId"] = value["target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentTargetInput:
    out: GetDeploymentTargetInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("GetDeploymentTargetInput.deployment_id required")
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("GetDeploymentTargetInput.target_id required")
    return out
