"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#CreateGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.group_name
    import aws_sdk_directory_service_data.types.sid


class CreateGroupResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory that's associated with the group. </p>"""
    sam_account_name: NotRequired[
        "aws_sdk_directory_service_data.types.group_name.GroupName"
    ]
    """<p> The name of the group. </p>"""
    sid: NotRequired["aws_sdk_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "sam_account_name" in value:
        out["SAMAccountName"] = value["sam_account_name"]
    if "sid" in value:
        out["SID"] = value["sid"]
    return out


def deserialize_json(data: dict) -> CreateGroupResult:
    out: CreateGroupResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    if "SID" in data:
        out["sid"] = data["SID"]
    return out
