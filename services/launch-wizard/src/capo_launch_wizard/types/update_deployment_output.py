"""Generated from Smithy shape ``com.amazonaws.launchwizard#UpdateDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_data_summary


class UpdateDeploymentOutput(TypedDict, closed=True):
    deployment: NotRequired[
        "capo_launch_wizard.types.deployment_data_summary.DeploymentDataSummary"
    ]
    """<p>The deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment" in value:
        import capo_launch_wizard.types.deployment_data_summary

        out["deployment"] = (
            capo_launch_wizard.types.deployment_data_summary.serialize_json(
                value["deployment"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDeploymentOutput:
    out: UpdateDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "deployment" in data:
        import capo_launch_wizard.types.deployment_data_summary

        out["deployment"] = (
            capo_launch_wizard.types.deployment_data_summary.deserialize_json(
                data["deployment"]
            )
        )
    return out
