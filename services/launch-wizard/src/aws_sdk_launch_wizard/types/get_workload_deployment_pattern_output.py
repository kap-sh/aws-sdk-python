"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetWorkloadDeploymentPatternOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.workload_deployment_pattern_data


class GetWorkloadDeploymentPatternOutput(TypedDict):
    workload_deployment_pattern: NotRequired[
        "aws_sdk_launch_wizard.types.workload_deployment_pattern_data.WorkloadDeploymentPatternData"
    ]
    """<p>Details about the workload deployment pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadDeploymentPatternOutput) -> dict:
    out: dict = {}
    if "workload_deployment_pattern" in value:
        import aws_sdk_launch_wizard.types.workload_deployment_pattern_data

        out["workloadDeploymentPattern"] = (
            aws_sdk_launch_wizard.types.workload_deployment_pattern_data.serialize_json(
                value["workload_deployment_pattern"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWorkloadDeploymentPatternOutput:
    out: GetWorkloadDeploymentPatternOutput = {}  # type: ignore[typeddict-item]
    if "workloadDeploymentPattern" in data:
        import aws_sdk_launch_wizard.types.workload_deployment_pattern_data

        out["workload_deployment_pattern"] = (
            aws_sdk_launch_wizard.types.workload_deployment_pattern_data.deserialize_json(
                data["workloadDeploymentPattern"]
            )
        )
    return out
