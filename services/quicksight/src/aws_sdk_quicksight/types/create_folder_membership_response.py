"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateFolderMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.folder_member
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class CreateFolderMembershipResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folder_member: NotRequired["aws_sdk_quicksight.types.folder_member.FolderMember"]
    """<p>Information about the member in the folder.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFolderMembershipResponse) -> dict:
    out: dict = {}
    out["Status"] = value.get("status", 0)
    if "folder_member" in value:
        import aws_sdk_quicksight.types.folder_member

        out["FolderMember"] = aws_sdk_quicksight.types.folder_member.serialize_json(
            value["folder_member"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateFolderMembershipResponse:
    out: CreateFolderMembershipResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    if "FolderMember" in data:
        import aws_sdk_quicksight.types.folder_member

        out["folder_member"] = aws_sdk_quicksight.types.folder_member.deserialize_json(
            data["FolderMember"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
