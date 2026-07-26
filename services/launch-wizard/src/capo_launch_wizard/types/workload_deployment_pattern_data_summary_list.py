"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDeploymentPatternDataSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.workload_deployment_pattern_data_summary

WorkloadDeploymentPatternDataSummaryList: TypeAlias = list[
    "capo_launch_wizard.types.workload_deployment_pattern_data_summary.WorkloadDeploymentPatternDataSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDeploymentPatternDataSummaryList) -> list:
    import capo_launch_wizard.types.workload_deployment_pattern_data_summary

    out: list = []
    for item in value:
        out.append(
            capo_launch_wizard.types.workload_deployment_pattern_data_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkloadDeploymentPatternDataSummaryList:
    import capo_launch_wizard.types.workload_deployment_pattern_data_summary

    out: WorkloadDeploymentPatternDataSummaryList = []
    for item in data:
        out.append(
            capo_launch_wizard.types.workload_deployment_pattern_data_summary.deserialize_json(
                item
            )
        )
    return out
