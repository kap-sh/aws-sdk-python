"""Generated from Smithy shape ``com.amazonaws.inspector2#ListMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.member_list
    import capo_inspector2.types.next_token


class ListMembersResponse(TypedDict, closed=True):
    members: NotRequired["capo_inspector2.types.member_list.MemberList"]
    """<p>An object that contains details for each member account.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import capo_inspector2.types.member_list

        out["members"] = capo_inspector2.types.member_list.serialize_json(
            value["members"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersResponse:
    out: ListMembersResponse = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import capo_inspector2.types.member_list

        out["members"] = capo_inspector2.types.member_list.deserialize_json(
            data["members"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
