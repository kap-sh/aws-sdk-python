"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeleteDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_status


class DeleteDeploymentOutput(TypedDict, closed=True):
    status: NotRequired["capo_launch_wizard.types.deployment_status.DeploymentStatus"]
    """<p>The status of the deployment.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the deployment status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeploymentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_launch_wizard.types.deployment_status

        out["status"] = capo_launch_wizard.types.deployment_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> DeleteDeploymentOutput:
    out: DeleteDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_launch_wizard.types.deployment_status

        out["status"] = capo_launch_wizard.types.deployment_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
