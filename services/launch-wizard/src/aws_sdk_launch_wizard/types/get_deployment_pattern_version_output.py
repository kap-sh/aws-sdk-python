"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetDeploymentPatternVersionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_pattern_version_data_summary


class GetDeploymentPatternVersionOutput(TypedDict):
    deployment_pattern_version: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_pattern_version_data_summary.DeploymentPatternVersionDataSummary"
    ]
    """<p>The deployment pattern version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentPatternVersionOutput) -> dict:
    out: dict = {}
    if "deployment_pattern_version" in value:
        import aws_sdk_launch_wizard.types.deployment_pattern_version_data_summary

        out["deploymentPatternVersion"] = (
            aws_sdk_launch_wizard.types.deployment_pattern_version_data_summary.serialize_json(
                value["deployment_pattern_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDeploymentPatternVersionOutput:
    out: GetDeploymentPatternVersionOutput = {}  # type: ignore[typeddict-item]
    if "deploymentPatternVersion" in data:
        import aws_sdk_launch_wizard.types.deployment_pattern_version_data_summary

        out["deployment_pattern_version"] = (
            aws_sdk_launch_wizard.types.deployment_pattern_version_data_summary.deserialize_json(
                data["deploymentPatternVersion"]
            )
        )
    return out
