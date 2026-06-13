"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateFolderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.folder_name
    import aws_sdk_quicksight.types.folder_type
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.restrictive_resource_id
    import aws_sdk_quicksight.types.sharing_model
    import aws_sdk_quicksight.types.tag_list


class CreateFolderRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account where you want to create the folder.</p>"""
    folder_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.folder_name.FolderName"]
    """<p>The name of the folder.</p>"""
    folder_type: NotRequired["aws_sdk_quicksight.types.folder_type.FolderType"]
    """<p>The type of folder. By default, <code>folderType</code> is <code>SHARED</code>.</p>"""
    parent_folder_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the parent folder.</p> <p> <code>ParentFolderArn</code> can be null. An empty <code>parentFolderArn</code> creates a root-level folder.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A structure that describes the principals and the resource-level permissions of a folder.</p> <p>To specify no permissions, omit <code>Permissions</code>.</p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>Tags for the folder.</p>"""
    sharing_model: NotRequired["aws_sdk_quicksight.types.sharing_model.SharingModel"]
    """<p>An optional parameter that determines the sharing scope of the folder. The default value for this parameter is <code>ACCOUNT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFolderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "folder_type" in value:
        import aws_sdk_quicksight.types.folder_type

        out["FolderType"] = aws_sdk_quicksight.types.folder_type.serialize_json(
            value["folder_type"]
        )
    if "parent_folder_arn" in value:
        out["ParentFolderArn"] = value["parent_folder_arn"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    if "sharing_model" in value:
        import aws_sdk_quicksight.types.sharing_model

        out["SharingModel"] = aws_sdk_quicksight.types.sharing_model.serialize_json(
            value["sharing_model"]
        )
    return out


def deserialize_json(data: dict) -> CreateFolderRequest:
    out: CreateFolderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "FolderType" in data:
        import aws_sdk_quicksight.types.folder_type

        out["folder_type"] = aws_sdk_quicksight.types.folder_type.deserialize_json(
            data["FolderType"]
        )
    if "ParentFolderArn" in data:
        out["parent_folder_arn"] = data["ParentFolderArn"]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if "SharingModel" in data:
        import aws_sdk_quicksight.types.sharing_model

        out["sharing_model"] = aws_sdk_quicksight.types.sharing_model.deserialize_json(
            data["SharingModel"]
        )
    return out
