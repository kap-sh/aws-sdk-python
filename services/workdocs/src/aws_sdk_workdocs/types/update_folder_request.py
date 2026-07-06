"""Generated from Smithy shape ``com.amazonaws.workdocs#UpdateFolderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.resource_name_type
    import aws_sdk_workdocs.types.resource_state_type


class UpdateFolderRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the folder.</p>"""
    name: NotRequired["aws_sdk_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the folder.</p>"""
    parent_folder_id: NotRequired[
        "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    ]
    """<p>The ID of the parent folder.</p>"""
    resource_state: NotRequired[
        "aws_sdk_workdocs.types.resource_state_type.ResourceStateType"
    ]
    """<p>The resource state of the folder. Only ACTIVE and RECYCLED are accepted values from the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFolderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "parent_folder_id" in value:
        out["ParentFolderId"] = value["parent_folder_id"]
    if "resource_state" in value:
        import aws_sdk_workdocs.types.resource_state_type

        out["ResourceState"] = (
            aws_sdk_workdocs.types.resource_state_type.serialize_json(
                value["resource_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFolderRequest:
    out: UpdateFolderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ParentFolderId" in data:
        out["parent_folder_id"] = data["ParentFolderId"]
    if "ResourceState" in data:
        import aws_sdk_workdocs.types.resource_state_type

        out["resource_state"] = (
            aws_sdk_workdocs.types.resource_state_type.deserialize_json(
                data["ResourceState"]
            )
        )
    return out
