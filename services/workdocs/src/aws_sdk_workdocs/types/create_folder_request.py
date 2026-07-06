"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateFolderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.resource_name_type


class CreateFolderRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    name: NotRequired["aws_sdk_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the new folder.</p>"""
    parent_folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the parent folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFolderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["ParentFolderId"] = value["parent_folder_id"]
    return out


def deserialize_json(data: dict) -> CreateFolderRequest:
    out: CreateFolderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ParentFolderId" in data:
        out["parent_folder_id"] = data["ParentFolderId"]
    else:
        raise DeserializationError("CreateFolderRequest.parent_folder_id required")
    return out
