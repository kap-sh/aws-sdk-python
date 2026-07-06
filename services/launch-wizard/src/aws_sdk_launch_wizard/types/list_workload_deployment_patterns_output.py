"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListWorkloadDeploymentPatternsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.next_token
    import aws_sdk_launch_wizard.types.workload_deployment_pattern_data_summary_list


class ListWorkloadDeploymentPatternsOutput(TypedDict, closed=True):
    workload_deployment_patterns: NotRequired[
        "aws_sdk_launch_wizard.types.workload_deployment_pattern_data_summary_list.WorkloadDeploymentPatternDataSummaryList"
    ]
    """<p>Describes the workload deployment patterns.</p>"""
    next_token: NotRequired["aws_sdk_launch_wizard.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadDeploymentPatternsOutput) -> dict:
    out: dict = {}
    if "workload_deployment_patterns" in value:
        import aws_sdk_launch_wizard.types.workload_deployment_pattern_data_summary_list

        out["workloadDeploymentPatterns"] = (
            aws_sdk_launch_wizard.types.workload_deployment_pattern_data_summary_list.serialize_json(
                value["workload_deployment_patterns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadDeploymentPatternsOutput:
    out: ListWorkloadDeploymentPatternsOutput = {}  # type: ignore[typeddict-item]
    if "workloadDeploymentPatterns" in data:
        import aws_sdk_launch_wizard.types.workload_deployment_pattern_data_summary_list

        out["workload_deployment_patterns"] = (
            aws_sdk_launch_wizard.types.workload_deployment_pattern_data_summary_list.deserialize_json(
                data["workloadDeploymentPatterns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
