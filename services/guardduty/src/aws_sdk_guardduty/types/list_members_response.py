"""Generated from Smithy shape ``com.amazonaws.guardduty#ListMembersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.members
    import aws_sdk_guardduty.types.string


class ListMembersResponse(TypedDict):
    members: NotRequired["aws_sdk_guardduty.types.members.Members"]
    """<p>A list of members.</p> <note> <p>The values for <code>email</code> and <code>invitedAt</code> are available only if the member accounts are added by invitation.</p> </note>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import aws_sdk_guardduty.types.members

        out["members"] = aws_sdk_guardduty.types.members.serialize_json(
            value["members"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersResponse:
    out: ListMembersResponse = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import aws_sdk_guardduty.types.members

        out["members"] = aws_sdk_guardduty.types.members.deserialize_json(
            data["members"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
