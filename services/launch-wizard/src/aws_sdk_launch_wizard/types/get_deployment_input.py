"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_id


class GetDeploymentInput(TypedDict, closed=True):
    deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_json(data: dict) -> GetDeploymentInput:
    out: GetDeploymentInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("GetDeploymentInput.deployment_id required")
    return out
