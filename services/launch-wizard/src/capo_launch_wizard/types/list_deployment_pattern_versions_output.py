"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListDeploymentPatternVersionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_version_data_summary_list
    import capo_launch_wizard.types.next_token


class ListDeploymentPatternVersionsOutput(TypedDict, closed=True):
    deployment_pattern_versions: NotRequired[
        "capo_launch_wizard.types.deployment_pattern_version_data_summary_list.DeploymentPatternVersionDataSummaryList"
    ]
    """<p>The deployment pattern versions.</p>"""
    next_token: NotRequired["capo_launch_wizard.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentPatternVersionsOutput) -> dict:
    out: dict = {}
    if "deployment_pattern_versions" in value:
        import capo_launch_wizard.types.deployment_pattern_version_data_summary_list

        out["deploymentPatternVersions"] = (
            capo_launch_wizard.types.deployment_pattern_version_data_summary_list.serialize_json(
                value["deployment_pattern_versions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentPatternVersionsOutput:
    out: ListDeploymentPatternVersionsOutput = {}  # type: ignore[typeddict-item]
    if "deploymentPatternVersions" in data:
        import capo_launch_wizard.types.deployment_pattern_version_data_summary_list

        out["deployment_pattern_versions"] = (
            capo_launch_wizard.types.deployment_pattern_version_data_summary_list.deserialize_json(
                data["deploymentPatternVersions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
