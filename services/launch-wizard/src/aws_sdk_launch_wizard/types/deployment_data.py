"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_launch_wizard.types.deployment_id
    import aws_sdk_launch_wizard.types.deployment_pattern_name
    import aws_sdk_launch_wizard.types.deployment_specifications
    import aws_sdk_launch_wizard.types.deployment_status
    import aws_sdk_launch_wizard.types.tags
    import aws_sdk_launch_wizard.types.workload_name


class DeploymentData(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the deployment.</p>"""
    id: NotRequired["aws_sdk_launch_wizard.types.deployment_id.DeploymentId"]
    """<p>The ID of the deployment.</p>"""
    workload_name: NotRequired["aws_sdk_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    pattern_name: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    ]
    """<p>The pattern name of the deployment.</p>"""
    status: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the deployment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time the deployment was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time the deployment was last modified.</p>"""
    specifications: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_specifications.DeploymentSpecifications"
    ]
    r"""<p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html\">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html\"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>"""
    resource_group: NotRequired["str"]
    """<p>The resource group of the deployment.</p>"""
    deleted_at: NotRequired["datetime.datetime"]
    """<p>The time the deployment was deleted.</p>"""
    tags: NotRequired["aws_sdk_launch_wizard.types.tags.Tags"]
    """<p>Information about the tags attached to a deployment.</p>"""
    deployment_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentData) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "pattern_name" in value:
        out["patternName"] = value["pattern_name"]
    if "status" in value:
        import aws_sdk_launch_wizard.types.deployment_status

        out["status"] = aws_sdk_launch_wizard.types.deployment_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["modifiedAt"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.serialize_json(
                value["modified_at"]
            )
        )
    if "specifications" in value:
        import aws_sdk_launch_wizard.types.deployment_specifications

        out["specifications"] = (
            aws_sdk_launch_wizard.types.deployment_specifications.serialize_json(
                value["specifications"]
            )
        )
    if "resource_group" in value:
        out["resourceGroup"] = value["resource_group"]
    if "deleted_at" in value:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["deletedAt"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.serialize_json(
                value["deleted_at"]
            )
        )
    if "tags" in value:
        import aws_sdk_launch_wizard.types.tags

        out["tags"] = aws_sdk_launch_wizard.types.tags.serialize_json(value["tags"])
    if "deployment_arn" in value:
        out["deploymentArn"] = value["deployment_arn"]
    return out


def deserialize_json(data: dict) -> DeploymentData:
    out: DeploymentData = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "workloadName" in data:
        out["workload_name"] = data["workloadName"]
    if "patternName" in data:
        out["pattern_name"] = data["patternName"]
    if "status" in data:
        import aws_sdk_launch_wizard.types.deployment_status

        out["status"] = aws_sdk_launch_wizard.types.deployment_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    if "specifications" in data:
        import aws_sdk_launch_wizard.types.deployment_specifications

        out["specifications"] = (
            aws_sdk_launch_wizard.types.deployment_specifications.deserialize_json(
                data["specifications"]
            )
        )
    if "resourceGroup" in data:
        out["resource_group"] = data["resourceGroup"]
    if "deletedAt" in data:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["deleted_at"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["deletedAt"]
            )
        )
    if "tags" in data:
        import aws_sdk_launch_wizard.types.tags

        out["tags"] = aws_sdk_launch_wizard.types.tags.deserialize_json(data["tags"])
    if "deploymentArn" in data:
        out["deployment_arn"] = data["deploymentArn"]
    return out
