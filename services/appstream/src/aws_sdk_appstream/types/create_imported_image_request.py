"""Generated from Smithy shape ``com.amazonaws.appstream#CreateImportedImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.agent_software_version
    import aws_sdk_appstream.types.app_catalog_config
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.boolean
    import aws_sdk_appstream.types.image_import_description
    import aws_sdk_appstream.types.image_import_display_name
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.photon_ami_id
    import aws_sdk_appstream.types.runtime_validation_config
    import aws_sdk_appstream.types.tags
    import aws_sdk_appstream.types.workspace_image_id


class CreateImportedImageRequest(TypedDict, closed=True):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>A unique name for the imported image. The name must be between 1 and 100 characters and can contain letters, numbers, underscores, periods, and hyphens.</p>"""
    source_ami_id: NotRequired["aws_sdk_appstream.types.photon_ami_id.PhotonAmiId"]
    """<p>The ID of the EC2 AMI to import.</p>"""
    workspace_image_id: NotRequired[
        "aws_sdk_appstream.types.workspace_image_id.WorkspaceImageId"
    ]
    """<p>The ID of the Workspaces Image to import.</p>"""
    iam_role_arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the IAM role that allows WorkSpaces Applications to access your AMI. The role must have permissions to modify image attributes and describe images, with a trust relationship allowing appstream.amazonaws.com to assume the role.</p>"""
    description: NotRequired[
        "aws_sdk_appstream.types.image_import_description.ImageImportDescription"
    ]
    """<p>An optional description for the imported image. The description must match approved regex patterns and can be up to 256 characters.</p>"""
    display_name: NotRequired[
        "aws_sdk_appstream.types.image_import_display_name.ImageImportDisplayName"
    ]
    """<p>An optional display name for the imported image. The display name must match approved regex patterns and can be up to 100 characters.</p>"""
    tags: NotRequired["aws_sdk_appstream.types.tags.Tags"]
    """<p>The tags to apply to the imported image. Tags help you organize and manage your WorkSpaces Applications resources.</p>"""
    runtime_validation_config: NotRequired[
        "aws_sdk_appstream.types.runtime_validation_config.RuntimeValidationConfig"
    ]
    """<p>Configuration for runtime validation of the imported image. When specified, WorkSpaces Applications provisions an instance to test streaming functionality, which helps ensure the image is suitable for use.</p>"""
    agent_software_version: NotRequired[
        "aws_sdk_appstream.types.agent_software_version.AgentSoftwareVersion"
    ]
    """<p>The version of the WorkSpaces Applications agent to use for the imported image. Choose CURRENT_LATEST to use the agent version available at the time of import, or ALWAYS_LATEST to automatically update to the latest agent version when new versions are released.</p>"""
    app_catalog_config: NotRequired[
        "aws_sdk_appstream.types.app_catalog_config.AppCatalogConfig"
    ]
    """<p>Configuration for the application catalog of the imported image. This allows you to specify applications available for streaming, including their paths, icons, and launch parameters. This field contains sensitive data.</p>"""
    dry_run: NotRequired["aws_sdk_appstream.types.boolean.Boolean"]
    """<p>When set to true, performs validation checks without actually creating the imported image. Use this to verify your configuration before executing the actual import operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImportedImageRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "source_ami_id" in value:
        out["SourceAmiId"] = value["source_ami_id"]
    if "workspace_image_id" in value:
        out["WorkspaceImageId"] = value["workspace_image_id"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "tags" in value:
        import aws_sdk_appstream.types.tags

        out["Tags"] = aws_sdk_appstream.types.tags.serialize_aws_json_1_1(value["tags"])
    if "runtime_validation_config" in value:
        import aws_sdk_appstream.types.runtime_validation_config

        out["RuntimeValidationConfig"] = (
            aws_sdk_appstream.types.runtime_validation_config.serialize_aws_json_1_1(
                value["runtime_validation_config"]
            )
        )
    if "agent_software_version" in value:
        import aws_sdk_appstream.types.agent_software_version

        out["AgentSoftwareVersion"] = (
            aws_sdk_appstream.types.agent_software_version.serialize_aws_json_1_1(
                value["agent_software_version"]
            )
        )
    if "app_catalog_config" in value:
        import aws_sdk_appstream.types.app_catalog_config

        out["AppCatalogConfig"] = (
            aws_sdk_appstream.types.app_catalog_config.serialize_aws_json_1_1(
                value["app_catalog_config"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImportedImageRequest:
    out: CreateImportedImageRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SourceAmiId" in data:
        out["source_ami_id"] = data["SourceAmiId"]
    if "WorkspaceImageId" in data:
        out["workspace_image_id"] = data["WorkspaceImageId"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Tags" in data:
        import aws_sdk_appstream.types.tags

        out["tags"] = aws_sdk_appstream.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "RuntimeValidationConfig" in data:
        import aws_sdk_appstream.types.runtime_validation_config

        out["runtime_validation_config"] = (
            aws_sdk_appstream.types.runtime_validation_config.deserialize_aws_json_1_1(
                data["RuntimeValidationConfig"]
            )
        )
    if "AgentSoftwareVersion" in data:
        import aws_sdk_appstream.types.agent_software_version

        out["agent_software_version"] = (
            aws_sdk_appstream.types.agent_software_version.deserialize_aws_json_1_1(
                data["AgentSoftwareVersion"]
            )
        )
    if "AppCatalogConfig" in data:
        import aws_sdk_appstream.types.app_catalog_config

        out["app_catalog_config"] = (
            aws_sdk_appstream.types.app_catalog_config.deserialize_aws_json_1_1(
                data["AppCatalogConfig"]
            )
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    return out
