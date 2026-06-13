"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetWorkloadDeploymentPatternInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_pattern_name
    import aws_sdk_launch_wizard.types.workload_name


class GetWorkloadDeploymentPatternInput(TypedDict):
    workload_name: "aws_sdk_launch_wizard.types.workload_name.WorkloadName"
    """<p>The name of the workload.</p>"""
    deployment_pattern_name: (
        "aws_sdk_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    )
    """<p>The name of the deployment pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadDeploymentPatternInput) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["deploymentPatternName"] = value["deployment_pattern_name"]
    return out


def deserialize_json(data: dict) -> GetWorkloadDeploymentPatternInput:
    out: GetWorkloadDeploymentPatternInput = {}  # type: ignore[typeddict-item]
    if "workloadName" in data:
        out["workload_name"] = data["workloadName"]
    else:
        raise DeserializationError(
            "GetWorkloadDeploymentPatternInput.workload_name required"
        )
    if "deploymentPatternName" in data:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    else:
        raise DeserializationError(
            "GetWorkloadDeploymentPatternInput.deployment_pattern_name required"
        )
    return out
