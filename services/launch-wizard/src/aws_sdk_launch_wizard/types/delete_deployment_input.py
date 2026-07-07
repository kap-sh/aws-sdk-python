"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeleteDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_id


class DeleteDeploymentInput(TypedDict, closed=True):
    deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeploymentInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_json(data: dict) -> DeleteDeploymentInput:
    out: DeleteDeploymentInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("DeleteDeploymentInput.deployment_id required")
    return out
