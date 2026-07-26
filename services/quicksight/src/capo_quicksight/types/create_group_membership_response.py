"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateGroupMembershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.group_member
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class CreateGroupMembershipResponse(TypedDict, closed=True):
    group_member: NotRequired["capo_quicksight.types.group_member.GroupMember"]
    """<p>The group member.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupMembershipResponse) -> dict:
    out: dict = {}
    if "group_member" in value:
        import capo_quicksight.types.group_member

        out["GroupMember"] = capo_quicksight.types.group_member.serialize_json(
            value["group_member"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateGroupMembershipResponse:
    out: CreateGroupMembershipResponse = {}  # type: ignore[typeddict-item]
    if "GroupMember" in data:
        import capo_quicksight.types.group_member

        out["group_member"] = capo_quicksight.types.group_member.deserialize_json(
            data["GroupMember"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
