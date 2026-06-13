"""Generated from Smithy shape ``com.amazonaws.quicksight#ListFolderMembersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.folder_member_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListFolderMembersResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folder_member_list: NotRequired[
        "aws_sdk_quicksight.types.folder_member_list.FolderMemberList"
    ]
    """<p>A structure that contains all of the folder members (dashboards, analyses, and datasets) in the folder.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFolderMembersResponse) -> dict:
    out: dict = {}
    if "folder_member_list" in value:
        import aws_sdk_quicksight.types.folder_member_list

        out["FolderMemberList"] = (
            aws_sdk_quicksight.types.folder_member_list.serialize_json(
                value["folder_member_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListFolderMembersResponse:
    out: ListFolderMembersResponse = {}  # type: ignore[typeddict-item]
    if "FolderMemberList" in data:
        import aws_sdk_quicksight.types.folder_member_list

        out["folder_member_list"] = (
            aws_sdk_quicksight.types.folder_member_list.deserialize_json(
                data["FolderMemberList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
