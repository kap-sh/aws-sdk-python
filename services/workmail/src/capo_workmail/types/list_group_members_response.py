"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.members
    import capo_workmail.types.next_token


class ListGroupMembersResponse(TypedDict, closed=True):
    members: NotRequired["capo_workmail.types.members.Members"]
    """<p>The members associated to the group.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import capo_workmail.types.members

        out["Members"] = capo_workmail.types.members.serialize_aws_json_1_1(
            value["members"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupMembersResponse:
    out: ListGroupMembersResponse = {}  # type: ignore[typeddict-item]
    if "Members" in data:
        import capo_workmail.types.members

        out["members"] = capo_workmail.types.members.deserialize_aws_json_1_1(
            data["Members"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
