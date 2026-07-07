"""Generated from Smithy shape ``com.amazonaws.quicksight#ListRoleMembershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.groups_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListRoleMembershipsResponse(TypedDict, closed=True):
    members_list: NotRequired["aws_sdk_quicksight.types.groups_list.GroupsList"]
    """<p>The list of groups associated with a role</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoleMembershipsResponse) -> dict:
    out: dict = {}
    if "members_list" in value:
        import aws_sdk_quicksight.types.groups_list

        out["MembersList"] = aws_sdk_quicksight.types.groups_list.serialize_json(
            value["members_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListRoleMembershipsResponse:
    out: ListRoleMembershipsResponse = {}  # type: ignore[typeddict-item]
    if "MembersList" in data:
        import aws_sdk_quicksight.types.groups_list

        out["members_list"] = aws_sdk_quicksight.types.groups_list.deserialize_json(
            data["MembersList"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
