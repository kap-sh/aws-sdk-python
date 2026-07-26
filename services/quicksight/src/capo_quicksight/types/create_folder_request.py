"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateFolderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.folder_name
    import capo_quicksight.types.folder_type
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.restrictive_resource_id
    import capo_quicksight.types.sharing_model
    import capo_quicksight.types.tag_list


class CreateFolderRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account where you want to create the folder.</p>"""
    folder_id: "capo_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""
    name: NotRequired["capo_quicksight.types.folder_name.FolderName"]
    """<p>The name of the folder.</p>"""
    folder_type: NotRequired["capo_quicksight.types.folder_type.FolderType"]
    """<p>The type of folder. By default, <code>folderType</code> is <code>SHARED</code>.</p>"""
    parent_folder_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the parent folder.</p> <p> <code>ParentFolderArn</code> can be null. An empty <code>parentFolderArn</code> creates a root-level folder.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A structure that describes the principals and the resource-level permissions of a folder.</p> <p>To specify no permissions, omit <code>Permissions</code>.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>Tags for the folder.</p>"""
    sharing_model: NotRequired["capo_quicksight.types.sharing_model.SharingModel"]
    """<p>An optional parameter that determines the sharing scope of the folder. The default value for this parameter is <code>ACCOUNT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFolderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "folder_type" in value:
        import capo_quicksight.types.folder_type

        out["FolderType"] = capo_quicksight.types.folder_type.serialize_json(
            value["folder_type"]
        )
    if "parent_folder_arn" in value:
        out["ParentFolderArn"] = value["parent_folder_arn"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    if "sharing_model" in value:
        import capo_quicksight.types.sharing_model

        out["SharingModel"] = capo_quicksight.types.sharing_model.serialize_json(
            value["sharing_model"]
        )
    return out


def deserialize_json(data: dict) -> CreateFolderRequest:
    out: CreateFolderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "FolderType" in data:
        import capo_quicksight.types.folder_type

        out["folder_type"] = capo_quicksight.types.folder_type.deserialize_json(
            data["FolderType"]
        )
    if "ParentFolderArn" in data:
        out["parent_folder_arn"] = data["ParentFolderArn"]
    if "Permissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "Tags" in data:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if "SharingModel" in data:
        import capo_quicksight.types.sharing_model

        out["sharing_model"] = capo_quicksight.types.sharing_model.deserialize_json(
            data["SharingModel"]
        )
    return out
