"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentPatternVersionDataSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_version_data_summary

DeploymentPatternVersionDataSummaryList: TypeAlias = list[
    "capo_launch_wizard.types.deployment_pattern_version_data_summary.DeploymentPatternVersionDataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPatternVersionDataSummaryList) -> list:
    import capo_launch_wizard.types.deployment_pattern_version_data_summary

    out: list = []
    for item in value:
        out.append(
            capo_launch_wizard.types.deployment_pattern_version_data_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeploymentPatternVersionDataSummaryList:
    import capo_launch_wizard.types.deployment_pattern_version_data_summary

    out: DeploymentPatternVersionDataSummaryList = []
    for item in data:
        out.append(
            capo_launch_wizard.types.deployment_pattern_version_data_summary.deserialize_json(
                item
            )
        )
    return out
