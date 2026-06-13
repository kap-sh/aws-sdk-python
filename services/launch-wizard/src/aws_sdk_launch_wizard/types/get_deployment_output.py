"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetDeploymentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_data


class GetDeploymentOutput(TypedDict):
    deployment: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_data.DeploymentData"
    ]
    """<p>An object that details the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment" in value:
        import aws_sdk_launch_wizard.types.deployment_data

        out["deployment"] = aws_sdk_launch_wizard.types.deployment_data.serialize_json(
            value["deployment"]
        )
    return out


def deserialize_json(data: dict) -> GetDeploymentOutput:
    out: GetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "deployment" in data:
        import aws_sdk_launch_wizard.types.deployment_data

        out["deployment"] = (
            aws_sdk_launch_wizard.types.deployment_data.deserialize_json(
                data["deployment"]
            )
        )
    return out
