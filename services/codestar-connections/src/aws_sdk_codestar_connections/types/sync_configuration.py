"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SyncConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.branch_name
    import aws_sdk_codestar_connections.types.deployment_file_path
    import aws_sdk_codestar_connections.types.iam_role_arn
    import aws_sdk_codestar_connections.types.owner_id
    import aws_sdk_codestar_connections.types.provider_type
    import aws_sdk_codestar_connections.types.publish_deployment_status
    import aws_sdk_codestar_connections.types.repository_link_id
    import aws_sdk_codestar_connections.types.repository_name
    import aws_sdk_codestar_connections.types.resource_name
    import aws_sdk_codestar_connections.types.sync_configuration_type
    import aws_sdk_codestar_connections.types.trigger_resource_update_on


class SyncConfiguration(TypedDict):
    branch: "aws_sdk_codestar_connections.types.branch_name.BranchName"
    """<p>The branch associated with a specific sync configuration.</p>"""
    config_file: NotRequired[
        "aws_sdk_codestar_connections.types.deployment_file_path.DeploymentFilePath"
    ]
    """<p>The file path to the configuration file associated with a specific sync configuration. The path should point to an actual file in the sync configurations linked repository.</p>"""
    owner_id: "aws_sdk_codestar_connections.types.owner_id.OwnerId"
    """<p>The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.</p>"""
    provider_type: "aws_sdk_codestar_connections.types.provider_type.ProviderType"
    """<p>The connection provider type associated with a specific sync configuration, such as GitHub.</p>"""
    repository_link_id: (
        "aws_sdk_codestar_connections.types.repository_link_id.RepositoryLinkId"
    )
    """<p>The ID of the repository link associated with a specific sync configuration.</p>"""
    repository_name: "aws_sdk_codestar_connections.types.repository_name.RepositoryName"
    """<p>The name of the repository associated with a specific sync configuration.</p>"""
    resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName"
    """<p>The name of the connection resource associated with a specific sync configuration.</p>"""
    role_arn: "aws_sdk_codestar_connections.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.</p>"""
    sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType"
    """<p>The type of sync for a specific sync configuration.</p>"""
    publish_deployment_status: NotRequired[
        "aws_sdk_codestar_connections.types.publish_deployment_status.PublishDeploymentStatus"
    ]
    """<p>Whether to enable or disable publishing of deployment status to source providers.</p>"""
    trigger_resource_update_on: NotRequired[
        "aws_sdk_codestar_connections.types.trigger_resource_update_on.TriggerResourceUpdateOn"
    ]
    """<p>When to trigger Git sync to begin the stack update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncConfiguration) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    if "config_file" in value:
        out["ConfigFile"] = value["config_file"]
    out["OwnerId"] = value["owner_id"]
    import aws_sdk_codestar_connections.types.provider_type

    out["ProviderType"] = (
        aws_sdk_codestar_connections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["RepositoryLinkId"] = value["repository_link_id"]
    out["RepositoryName"] = value["repository_name"]
    out["ResourceName"] = value["resource_name"]
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


def deserialize_aws_json_1_0(data: dict) -> SyncConfiguration:
    out: SyncConfiguration = {}  # type: ignore[typeddict-item]
    if "Branch" in data:
        out["branch"] = data["Branch"]
    else:
        raise DeserializationError("SyncConfiguration.branch required")
    if "ConfigFile" in data:
        out["config_file"] = data["ConfigFile"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    else:
        raise DeserializationError("SyncConfiguration.owner_id required")
    if "ProviderType" in data:
        import aws_sdk_codestar_connections.types.provider_type

        out["provider_type"] = (
            aws_sdk_codestar_connections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        raise DeserializationError("SyncConfiguration.provider_type required")
    if "RepositoryLinkId" in data:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        raise DeserializationError("SyncConfiguration.repository_link_id required")
    if "RepositoryName" in data:
        out["repository_name"] = data["RepositoryName"]
    else:
        raise DeserializationError("SyncConfiguration.repository_name required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("SyncConfiguration.resource_name required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("SyncConfiguration.role_arn required")
    if "SyncType" in data:
        import aws_sdk_codestar_connections.types.sync_configuration_type

        out["sync_type"] = (
            aws_sdk_codestar_connections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("SyncConfiguration.sync_type required")
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
