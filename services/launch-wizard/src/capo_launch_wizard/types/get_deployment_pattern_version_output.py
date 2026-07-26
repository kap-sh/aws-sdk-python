"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetDeploymentPatternVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_version_data_summary


class GetDeploymentPatternVersionOutput(TypedDict, closed=True):
    deployment_pattern_version: NotRequired[
        "capo_launch_wizard.types.deployment_pattern_version_data_summary.DeploymentPatternVersionDataSummary"
    ]
    """<p>The deployment pattern version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentPatternVersionOutput) -> dict:
    out: dict = {}
    if "deployment_pattern_version" in value:
        import capo_launch_wizard.types.deployment_pattern_version_data_summary

        out["deploymentPatternVersion"] = (
            capo_launch_wizard.types.deployment_pattern_version_data_summary.serialize_json(
                value["deployment_pattern_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDeploymentPatternVersionOutput:
    out: GetDeploymentPatternVersionOutput = {}  # type: ignore[typeddict-item]
    if "deploymentPatternVersion" in data:
        import capo_launch_wizard.types.deployment_pattern_version_data_summary

        out["deployment_pattern_version"] = (
            capo_launch_wizard.types.deployment_pattern_version_data_summary.deserialize_json(
                data["deploymentPatternVersion"]
            )
        )
    return out
