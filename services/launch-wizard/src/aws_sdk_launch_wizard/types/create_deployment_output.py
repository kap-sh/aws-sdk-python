"""Generated from Smithy shape ``com.amazonaws.launchwizard#CreateDeploymentOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_id

class CreateDeploymentOutput(TypedDict):
    deployment_id: NotRequired["aws_sdk_launch_wizard.types.deployment_id.DeploymentId"]
    """<p>The ID of the deployment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentOutput:
    out: CreateDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    return out