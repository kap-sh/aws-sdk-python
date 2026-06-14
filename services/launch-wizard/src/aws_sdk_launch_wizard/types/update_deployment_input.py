"""Generated from Smithy shape ``com.amazonaws.launchwizard#UpdateDeploymentInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_id
    import aws_sdk_launch_wizard.types.deployment_pattern_version_name
    import aws_sdk_launch_wizard.types.deployment_specifications
    import aws_sdk_launch_wizard.types.workload_version_name


class UpdateDeploymentInput(TypedDict):
    deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""
    specifications: (
        "aws_sdk_launch_wizard.types.deployment_specifications.DeploymentSpecifications"
    )
    r"""<p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html\">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html\"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>"""
    workload_version_name: NotRequired[
        "aws_sdk_launch_wizard.types.workload_version_name.WorkloadVersionName"
    ]
    """<p>The name of the workload version.</p>"""
    deployment_pattern_version_name: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
    ]
    """<p>The name of the deployment pattern version.</p>"""
    dry_run: "bool"
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    force: "bool"
    """<p>Forces the update even if validation warnings are present.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeploymentInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    import aws_sdk_launch_wizard.types.deployment_specifications

    out["specifications"] = (
        aws_sdk_launch_wizard.types.deployment_specifications.serialize_json(
            value["specifications"]
        )
    )
    if "workload_version_name" in value:
        out["workloadVersionName"] = value["workload_version_name"]
    if "deployment_pattern_version_name" in value:
        out["deploymentPatternVersionName"] = value["deployment_pattern_version_name"]
    out["dryRun"] = value.get("dry_run", False)
    out["force"] = value.get("force", False)
    return out


def deserialize_json(data: dict) -> UpdateDeploymentInput:
    out: UpdateDeploymentInput = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    else:
        raise DeserializationError("UpdateDeploymentInput.deployment_id required")
    if "specifications" in data:
        import aws_sdk_launch_wizard.types.deployment_specifications

        out["specifications"] = (
            aws_sdk_launch_wizard.types.deployment_specifications.deserialize_json(
                data["specifications"]
            )
        )
    else:
        raise DeserializationError("UpdateDeploymentInput.specifications required")
    if "workloadVersionName" in data:
        out["workload_version_name"] = data["workloadVersionName"]
    if "deploymentPatternVersionName" in data:
        out["deployment_pattern_version_name"] = data["deploymentPatternVersionName"]
    if "dryRun" in data:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    if "force" in data:
        out["force"] = data["force"]
    else:
        out["force"] = False
    return out
