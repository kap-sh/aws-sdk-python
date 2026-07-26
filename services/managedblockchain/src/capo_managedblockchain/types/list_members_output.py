"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListMembersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.member_summary_list
    import capo_managedblockchain.types.pagination_token


class ListMembersOutput(TypedDict, closed=True):
    members: NotRequired[
        "capo_managedblockchain.types.member_summary_list.MemberSummaryList"
    ]
    """<p>An array of <code>MemberSummary</code> objects. Each object contains details about a network member.</p>"""
    next_token: NotRequired[
        "capo_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersOutput) -> dict:
    out: dict = {}
    if "members" in value:
        import capo_managedblockchain.types.member_summary_list

        out["Members"] = (
            capo_managedblockchain.types.member_summary_list.serialize_json(
                value["members"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersOutput:
    out: ListMembersOutput = {}  # type: ignore[typeddict-item]
    if "Members" in data:
        import capo_managedblockchain.types.member_summary_list

        out["members"] = (
            capo_managedblockchain.types.member_summary_list.deserialize_json(
                data["Members"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
