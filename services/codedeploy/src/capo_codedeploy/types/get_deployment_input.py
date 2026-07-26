"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id


class GetDeploymentInput(TypedDict, closed=True):
    deployment_id: "capo_codedeploy.types.deployment_id.DeploymentId"
    """<p> The unique ID of a deployment associated with the user or Amazon Web Services account. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeploymentInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeploymentInput:
    out: GetDeploymentInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("GetDeploymentInput.deployment_id required")
    return out
