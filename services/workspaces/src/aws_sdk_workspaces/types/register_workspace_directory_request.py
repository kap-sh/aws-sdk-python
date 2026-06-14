"""Generated from Smithy shape ``com.amazonaws.workspaces#RegisterWorkspaceDirectoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.active_directory_config
    import aws_sdk_workspaces.types.arn
    import aws_sdk_workspaces.types.boolean_object
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.microsoft_entra_config
    import aws_sdk_workspaces.types.subnet_ids
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.tenancy
    import aws_sdk_workspaces.types.user_identity_type
    import aws_sdk_workspaces.types.workspace_directory_description
    import aws_sdk_workspaces.types.workspace_directory_name
    import aws_sdk_workspaces.types.workspace_type


class RegisterWorkspaceDirectoryRequest(TypedDict):
    directory_id: NotRequired["aws_sdk_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory. You cannot register a directory if it does not have a status of Active. If the directory does not have a status of Active, you will receive an InvalidResourceStateException error. If you have already registered the maximum number of directories that you can register with Amazon WorkSpaces, you will receive a ResourceLimitExceededException error. Deregister directories that you are not using for WorkSpaces, and try again.</p>"""
    subnet_ids: NotRequired["aws_sdk_workspaces.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets for your virtual private cloud (VPC). Make sure that the subnets are in supported Availability Zones. The subnets must also be in separate Availability Zones. If these conditions are not met, you will receive an OperationNotSupportedException error.</p>"""
    enable_self_service: NotRequired[
        "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether self-service capabilities are enabled or disabled.</p>"""
    tenancy: NotRequired["aws_sdk_workspaces.types.tenancy.Tenancy"]
    r"""<p>Indicates whether your WorkSpace directory is dedicated or shared. To use Bring Your Own License (BYOL) images, this value must be set to <code>DEDICATED</code> and your Amazon Web Services account must be enabled for BYOL. If your account has not been enabled for BYOL, you will receive an InvalidParameterValuesException error. For more information about BYOL images, see <a href=\"https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html\">Bring Your Own Windows Desktop Images</a>.</p>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags associated with the directory.</p>"""
    workspace_directory_name: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_name.WorkspaceDirectoryName"
    ]
    """<p>The name of the directory to register.</p>"""
    workspace_directory_description: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_description.WorkspaceDirectoryDescription"
    ]
    """<p>Description of the directory to register.</p>"""
    user_identity_type: NotRequired[
        "aws_sdk_workspaces.types.user_identity_type.UserIdentityType"
    ]
    """<p>The type of identity management the user is using.</p>"""
    idc_instance_arn: NotRequired["aws_sdk_workspaces.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the identity center instance.</p>"""
    microsoft_entra_config: NotRequired[
        "aws_sdk_workspaces.types.microsoft_entra_config.MicrosoftEntraConfig"
    ]
    """<p>The details about Microsoft Entra config.</p>"""
    workspace_type: NotRequired["aws_sdk_workspaces.types.workspace_type.WorkspaceType"]
    """<p>Indicates whether the directory's WorkSpace type is personal or pools.</p>"""
    active_directory_config: NotRequired[
        "aws_sdk_workspaces.types.active_directory_config.ActiveDirectoryConfig"
    ]
    """<p>The active directory config of the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterWorkspaceDirectoryRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "subnet_ids" in value:
        import aws_sdk_workspaces.types.subnet_ids

        out["SubnetIds"] = aws_sdk_workspaces.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "enable_self_service" in value:
        out["EnableSelfService"] = value["enable_self_service"]
    if "tenancy" in value:
        import aws_sdk_workspaces.types.tenancy

        out["Tenancy"] = aws_sdk_workspaces.types.tenancy.serialize_aws_json_1_1(
            value["tenancy"]
        )
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "workspace_directory_name" in value:
        out["WorkspaceDirectoryName"] = value["workspace_directory_name"]
    if "workspace_directory_description" in value:
        out["WorkspaceDirectoryDescription"] = value["workspace_directory_description"]
    if "user_identity_type" in value:
        import aws_sdk_workspaces.types.user_identity_type

        out["UserIdentityType"] = (
            aws_sdk_workspaces.types.user_identity_type.serialize_aws_json_1_1(
                value["user_identity_type"]
            )
        )
    if "idc_instance_arn" in value:
        out["IdcInstanceArn"] = value["idc_instance_arn"]
    if "microsoft_entra_config" in value:
        import aws_sdk_workspaces.types.microsoft_entra_config

        out["MicrosoftEntraConfig"] = (
            aws_sdk_workspaces.types.microsoft_entra_config.serialize_aws_json_1_1(
                value["microsoft_entra_config"]
            )
        )
    if "workspace_type" in value:
        import aws_sdk_workspaces.types.workspace_type

        out["WorkspaceType"] = (
            aws_sdk_workspaces.types.workspace_type.serialize_aws_json_1_1(
                value["workspace_type"]
            )
        )
    if "active_directory_config" in value:
        import aws_sdk_workspaces.types.active_directory_config

        out["ActiveDirectoryConfig"] = (
            aws_sdk_workspaces.types.active_directory_config.serialize_aws_json_1_1(
                value["active_directory_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterWorkspaceDirectoryRequest:
    out: RegisterWorkspaceDirectoryRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "SubnetIds" in data:
        import aws_sdk_workspaces.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_workspaces.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    if "EnableSelfService" in data:
        out["enable_self_service"] = data["EnableSelfService"]
    if "Tenancy" in data:
        import aws_sdk_workspaces.types.tenancy

        out["tenancy"] = aws_sdk_workspaces.types.tenancy.deserialize_aws_json_1_1(
            data["Tenancy"]
        )
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "WorkspaceDirectoryName" in data:
        out["workspace_directory_name"] = data["WorkspaceDirectoryName"]
    if "WorkspaceDirectoryDescription" in data:
        out["workspace_directory_description"] = data["WorkspaceDirectoryDescription"]
    if "UserIdentityType" in data:
        import aws_sdk_workspaces.types.user_identity_type

        out["user_identity_type"] = (
            aws_sdk_workspaces.types.user_identity_type.deserialize_aws_json_1_1(
                data["UserIdentityType"]
            )
        )
    if "IdcInstanceArn" in data:
        out["idc_instance_arn"] = data["IdcInstanceArn"]
    if "MicrosoftEntraConfig" in data:
        import aws_sdk_workspaces.types.microsoft_entra_config

        out["microsoft_entra_config"] = (
            aws_sdk_workspaces.types.microsoft_entra_config.deserialize_aws_json_1_1(
                data["MicrosoftEntraConfig"]
            )
        )
    if "WorkspaceType" in data:
        import aws_sdk_workspaces.types.workspace_type

        out["workspace_type"] = (
            aws_sdk_workspaces.types.workspace_type.deserialize_aws_json_1_1(
                data["WorkspaceType"]
            )
        )
    if "ActiveDirectoryConfig" in data:
        import aws_sdk_workspaces.types.active_directory_config

        out["active_directory_config"] = (
            aws_sdk_workspaces.types.active_directory_config.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfig"]
            )
        )
    return out
