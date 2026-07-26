"""Generated from Smithy shape ``com.amazonaws.quicksight#ListGroupMembershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.group_member_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class ListGroupMembershipsResponse(TypedDict, closed=True):
    group_member_list: NotRequired[
        "capo_quicksight.types.group_member_list.GroupMemberList"
    ]
    """<p>The list of the members of the group.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupMembershipsResponse) -> dict:
    out: dict = {}
    if "group_member_list" in value:
        import capo_quicksight.types.group_member_list

        out["GroupMemberList"] = capo_quicksight.types.group_member_list.serialize_json(
            value["group_member_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListGroupMembershipsResponse:
    out: ListGroupMembershipsResponse = {}  # type: ignore[typeddict-item]
    if "GroupMemberList" in data:
        import capo_quicksight.types.group_member_list

        out["group_member_list"] = (
            capo_quicksight.types.group_member_list.deserialize_json(
                data["GroupMemberList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
