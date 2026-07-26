"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateSyncConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_connections.types.branch_name
    import capo_codestar_connections.types.deployment_file_path
    import capo_codestar_connections.types.iam_role_arn
    import capo_codestar_connections.types.publish_deployment_status
    import capo_codestar_connections.types.repository_link_id
    import capo_codestar_connections.types.resource_name
    import capo_codestar_connections.types.sync_configuration_type
    import capo_codestar_connections.types.trigger_resource_update_on


class CreateSyncConfigurationInput(TypedDict, closed=True):
    branch: "capo_codestar_connections.types.branch_name.BranchName"
    """<p>The branch in the repository from which changes will be synced.</p>"""
    config_file: (
        "capo_codestar_connections.types.deployment_file_path.DeploymentFilePath"
    )
    """<p>The file name of the configuration file that manages syncing between the connection and the repository. This configuration file is stored in the repository.</p>"""
    repository_link_id: (
        "capo_codestar_connections.types.repository_link_id.RepositoryLinkId"
    )
    """<p>The ID of the repository link created for the connection. A repository link allows Git sync to monitor and sync changes to files in a specified Git repository.</p>"""
    resource_name: "capo_codestar_connections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource (for example, a CloudFormation stack in the case of CFN_STACK_SYNC) that will be synchronized from the linked repository.</p>"""
    role_arn: "capo_codestar_connections.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role that grants permission for Amazon Web Services to use Git sync to update a given Amazon Web Services resource on your behalf.</p>"""
    sync_type: (
        "capo_codestar_connections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The type of sync configuration.</p>"""
    publish_deployment_status: NotRequired[
        "capo_codestar_connections.types.publish_deployment_status.PublishDeploymentStatus"
    ]
    """<p>Whether to enable or disable publishing of deployment status to source providers.</p>"""
    trigger_resource_update_on: NotRequired[
        "capo_codestar_connections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
    ]
    """<p>When to trigger Git sync to begin the stack update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSyncConfigurationInput) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    out["ConfigFile"] = value["config_file"]
    out["RepositoryLinkId"] = value["repository_link_id"]
    out["ResourceName"] = value["resource_name"]
    out["RoleArn"] = value["role_arn"]
    import capo_codestar_connections.types.sync_configuration_type

    out["SyncType"] = (
        capo_codestar_connections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    if "publish_deployment_status" in value:
        import capo_codestar_connections.types.publish_deployment_status

        out["PublishDeploymentStatus"] = (
            capo_codestar_connections.types.publish_deployment_status.serialize_aws_json_1_0(
                value["publish_deployment_status"]
            )
        )
    if "trigger_resource_update_on" in value:
        import capo_codestar_connections.types.trigger_resource_update_on

        out["TriggerResourceUpdateOn"] = (
            capo_codestar_connections.types.trigger_resource_update_on.serialize_aws_json_1_0(
                value["trigger_resource_update_on"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSyncConfigurationInput:
    out: CreateSyncConfigurationInput = {}  # type: ignore[typeddict-item]
    if "Branch" in data:
        out["branch"] = data["Branch"]
    else:
        raise DeserializationError("CreateSyncConfigurationInput.branch required")
    if "ConfigFile" in data:
        out["config_file"] = data["ConfigFile"]
    else:
        raise DeserializationError("CreateSyncConfigurationInput.config_file required")
    if "RepositoryLinkId" in data:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        raise DeserializationError(
            "CreateSyncConfigurationInput.repository_link_id required"
        )
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError(
            "CreateSyncConfigurationInput.resource_name required"
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateSyncConfigurationInput.role_arn required")
    if "SyncType" in data:
        import capo_codestar_connections.types.sync_configuration_type

        out["sync_type"] = (
            capo_codestar_connections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("CreateSyncConfigurationInput.sync_type required")
    if "PublishDeploymentStatus" in data:
        import capo_codestar_connections.types.publish_deployment_status

        out["publish_deployment_status"] = (
            capo_codestar_connections.types.publish_deployment_status.deserialize_aws_json_1_0(
                data["PublishDeploymentStatus"]
            )
        )
    if "TriggerResourceUpdateOn" in data:
        import capo_codestar_connections.types.trigger_resource_update_on

        out["trigger_resource_update_on"] = (
            capo_codestar_connections.types.trigger_resource_update_on.deserialize_aws_json_1_0(
                data["TriggerResourceUpdateOn"]
            )
        )
    return out
