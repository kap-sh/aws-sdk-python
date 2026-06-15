"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDeploymentPatternData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_pattern_name
    import aws_sdk_launch_wizard.types.deployment_pattern_version_name
    import aws_sdk_launch_wizard.types.deployment_specifications_data
    import aws_sdk_launch_wizard.types.workload_deployment_pattern_status
    import aws_sdk_launch_wizard.types.workload_name
    import aws_sdk_launch_wizard.types.workload_version_name


class WorkloadDeploymentPatternData(TypedDict):
    workload_name: NotRequired["aws_sdk_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The workload name of the deployment pattern.</p>"""
    deployment_pattern_name: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    ]
    """<p>The name of the deployment pattern.</p>"""
    workload_version_name: NotRequired[
        "aws_sdk_launch_wizard.types.workload_version_name.WorkloadVersionName"
    ]
    """<p>The workload version name of the deployment pattern.</p>"""
    deployment_pattern_version_name: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
    ]
    """<p>The version name of the deployment pattern.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the deployment pattern.</p>"""
    description: NotRequired["str"]
    """<p>The description of the deployment pattern.</p>"""
    status: NotRequired[
        "aws_sdk_launch_wizard.types.workload_deployment_pattern_status.WorkloadDeploymentPatternStatus"
    ]
    """<p>The status of the deployment pattern.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of the deployment pattern.</p>"""
    specifications: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_specifications_data.DeploymentSpecificationsData"
    ]
    r"""<p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html\">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html\"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadDeploymentPatternData) -> dict:
    out: dict = {}
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "deployment_pattern_name" in value:
        out["deploymentPatternName"] = value["deployment_pattern_name"]
    if "workload_version_name" in value:
        out["workloadVersionName"] = value["workload_version_name"]
    if "deployment_pattern_version_name" in value:
        out["deploymentPatternVersionName"] = value["deployment_pattern_version_name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_launch_wizard.types.workload_deployment_pattern_status

        out["status"] = (
            aws_sdk_launch_wizard.types.workload_deployment_pattern_status.serialize_json(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "specifications" in value:
        import aws_sdk_launch_wizard.types.deployment_specifications_data

        out["specifications"] = (
            aws_sdk_launch_wizard.types.deployment_specifications_data.serialize_json(
                value["specifications"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkloadDeploymentPatternData:
    out: WorkloadDeploymentPatternData = {}  # type: ignore[typeddict-item]
    if "workloadName" in data:
        out["workload_name"] = data["workloadName"]
    if "deploymentPatternName" in data:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    if "workloadVersionName" in data:
        out["workload_version_name"] = data["workloadVersionName"]
    if "deploymentPatternVersionName" in data:
        out["deployment_pattern_version_name"] = data["deploymentPatternVersionName"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_launch_wizard.types.workload_deployment_pattern_status

        out["status"] = (
            aws_sdk_launch_wizard.types.workload_deployment_pattern_status.deserialize_json(
                data["status"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "specifications" in data:
        import aws_sdk_launch_wizard.types.deployment_specifications_data

        out["specifications"] = (
            aws_sdk_launch_wizard.types.deployment_specifications_data.deserialize_json(
                data["specifications"]
            )
        )
    return out
