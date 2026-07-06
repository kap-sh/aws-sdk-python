"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.boolean_object
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.ipv6_address
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.user_name
    import aws_sdk_workspaces.types.volume_encryption_key
    import aws_sdk_workspaces.types.workspace_name
    import aws_sdk_workspaces.types.workspace_properties


class WorkspaceRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the Directory Service directory for the WorkSpace. You can use <a>DescribeWorkspaceDirectories</a> to list the available directories.</p>"""
    user_name: "aws_sdk_workspaces.types.user_name.UserName"
    """<p>The user name of the user for the WorkSpace. This user name must exist in the Directory Service directory for the WorkSpace.</p> <p>The username is not case-sensitive, but we recommend matching the case in the Directory Service directory to avoid potential incompatibilities.</p> <p>The reserved keyword, <code>[UNDEFINED]</code>, is used when creating user-decoupled WorkSpaces.</p>"""
    bundle_id: "aws_sdk_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the bundle for the WorkSpace. You can use <a>DescribeWorkspaceBundles</a> to list the available bundles.</p>"""
    volume_encryption_key: NotRequired[
        "aws_sdk_workspaces.types.volume_encryption_key.VolumeEncryptionKey"
    ]
    """<p>The ARN of the symmetric KMS key used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric KMS keys.</p>"""
    user_volume_encryption_enabled: NotRequired[
        "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether the data stored on the user volume is encrypted.</p>"""
    root_volume_encryption_enabled: NotRequired[
        "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether the data stored on the root volume is encrypted.</p>"""
    workspace_properties: NotRequired[
        "aws_sdk_workspaces.types.workspace_properties.WorkspaceProperties"
    ]
    """<p>The WorkSpace properties.</p>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags for the WorkSpace.</p>"""
    workspace_name: NotRequired["aws_sdk_workspaces.types.workspace_name.WorkspaceName"]
    """<p>The name of the user-decoupled WorkSpace.</p> <note> <p> <code>WorkspaceName</code> is required if <code>UserName</code> is <code>[UNDEFINED]</code> for user-decoupled WorkSpaces. <code>WorkspaceName</code> is not applicable if <code>UserName</code> is specified for user-assigned WorkSpaces.</p> </note>"""
    ipv6_address: NotRequired["aws_sdk_workspaces.types.ipv6_address.Ipv6Address"]
    """<p>The IPv6 address for the WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["UserName"] = value["user_name"]
    out["BundleId"] = value["bundle_id"]
    if "volume_encryption_key" in value:
        out["VolumeEncryptionKey"] = value["volume_encryption_key"]
    if "user_volume_encryption_enabled" in value:
        out["UserVolumeEncryptionEnabled"] = value["user_volume_encryption_enabled"]
    if "root_volume_encryption_enabled" in value:
        out["RootVolumeEncryptionEnabled"] = value["root_volume_encryption_enabled"]
    if "workspace_properties" in value:
        import aws_sdk_workspaces.types.workspace_properties

        out["WorkspaceProperties"] = (
            aws_sdk_workspaces.types.workspace_properties.serialize_aws_json_1_1(
                value["workspace_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "workspace_name" in value:
        out["WorkspaceName"] = value["workspace_name"]
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceRequest:
    out: WorkspaceRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("WorkspaceRequest.directory_id required")
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("WorkspaceRequest.user_name required")
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    else:
        raise DeserializationError("WorkspaceRequest.bundle_id required")
    if "VolumeEncryptionKey" in data:
        out["volume_encryption_key"] = data["VolumeEncryptionKey"]
    if "UserVolumeEncryptionEnabled" in data:
        out["user_volume_encryption_enabled"] = data["UserVolumeEncryptionEnabled"]
    if "RootVolumeEncryptionEnabled" in data:
        out["root_volume_encryption_enabled"] = data["RootVolumeEncryptionEnabled"]
    if "WorkspaceProperties" in data:
        import aws_sdk_workspaces.types.workspace_properties

        out["workspace_properties"] = (
            aws_sdk_workspaces.types.workspace_properties.deserialize_aws_json_1_1(
                data["WorkspaceProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "WorkspaceName" in data:
        out["workspace_name"] = data["WorkspaceName"]
    if "Ipv6Address" in data:
        out["ipv6_address"] = data["Ipv6Address"]
    return out
