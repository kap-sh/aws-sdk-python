"""Generated from Smithy shape ``com.amazonaws.codestarconnections#UpdateSyncConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.branch_name
    import aws_sdk_codestar_connections.types.deployment_file_path
    import aws_sdk_codestar_connections.types.iam_role_arn
    import aws_sdk_codestar_connections.types.publish_deployment_status
    import aws_sdk_codestar_connections.types.repository_link_id
    import aws_sdk_codestar_connections.types.resource_name
    import aws_sdk_codestar_connections.types.sync_configuration_type
    import aws_sdk_codestar_connections.types.trigger_resource_update_on


class UpdateSyncConfigurationInput(TypedDict):
    branch: NotRequired["aws_sdk_codestar_connections.types.branch_name.BranchName"]
    """<p>The branch for the sync configuration to be updated.</p>"""
    config_file: NotRequired[
        "aws_sdk_codestar_connections.types.deployment_file_path.DeploymentFilePath"
    ]
    """<p>The configuration file for the sync configuration to be updated.</p>"""
    repository_link_id: NotRequired[
        "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId"
    ]
    """<p>The ID of the repository link for the sync configuration to be updated.</p>"""
    resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource for the sync configuration to be updated.</p>"""
    role_arn: NotRequired["aws_sdk_codestar_connections.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the IAM role for the sync configuration to be updated.</p>"""
    sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType"
    """<p>The sync type for the sync configuration to be updated.</p>"""
    publish_deployment_status: NotRequired[
        "aws_sdk_codestar_connections.types.publish_deployment_status.PublishDeploymentStatus"
    ]
    """<p>Whether to enable or disable publishing of deployment status to source providers.</p>"""
    trigger_resource_update_on: NotRequired[
        "aws_sdk_codestar_connections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
    ]
    """<p>When to trigger Git sync to begin the stack update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSyncConfigurationInput) -> dict:
    out: dict = {}
    if "branch" in value:
        out["Branch"] = value["branch"]
    if "config_file" in value:
        out["ConfigFile"] = value["config_file"]
    if "repository_link_id" in value:
        out["RepositoryLinkId"] = value["repository_link_id"]
    out["ResourceName"] = value["resource_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    import aws_sdk_codestar_connections.types.sync_configuration_type

    out["SyncType"] = (
        aws_sdk_codestar_connections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    if "publish_deployment_status" in value:
        import aws_sdk_codestar_connections.types.publish_deployment_status

        out["PublishDeploymentStatus"] = (
            aws_sdk_codestar_connections.types.publish_deployment_status.serialize_aws_json_1_0(
                value["publish_deployment_status"]
            )
        )
    if "trigger_resource_update_on" in value:
        import aws_sdk_codestar_connections.types.trigger_resource_update_on

        out["TriggerResourceUpdateOn"] = (
            aws_sdk_codestar_connections.types.trigger_resource_update_on.serialize_aws_json_1_0(
                value["trigger_resource_update_on"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSyncConfigurationInput:
    out: UpdateSyncConfigurationInput = {}  # type: ignore[typeddict-item]
    if "Branch" in data:
        out["branch"] = data["Branch"]
    if "ConfigFile" in data:
        out["config_file"] = data["ConfigFile"]
    if "RepositoryLinkId" in data:
        out["repository_link_id"] = data["RepositoryLinkId"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError(
            "UpdateSyncConfigurationInput.resource_name required"
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "SyncType" in data:
        import aws_sdk_codestar_connections.types.sync_configuration_type

        out["sync_type"] = (
            aws_sdk_codestar_connections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("UpdateSyncConfigurationInput.sync_type required")
    if "PublishDeploymentStatus" in data:
        import aws_sdk_codestar_connections.types.publish_deployment_status

        out["publish_deployment_status"] = (
            aws_sdk_codestar_connections.types.publish_deployment_status.deserialize_aws_json_1_0(
                data["PublishDeploymentStatus"]
            )
        )
    if "TriggerResourceUpdateOn" in data:
        import aws_sdk_codestar_connections.types.trigger_resource_update_on

        out["trigger_resource_update_on"] = (
            aws_sdk_codestar_connections.types.trigger_resource_update_on.deserialize_aws_json_1_0(
                data["TriggerResourceUpdateOn"]
            )
        )
    return out
