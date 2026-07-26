"""Generated from Smithy shape ``com.amazonaws.synthetics#ListAssociatedGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.group_summary_list
    import capo_synthetics.types.pagination_token


class ListAssociatedGroupsResponse(TypedDict, closed=True):
    groups: NotRequired["capo_synthetics.types.group_summary_list.GroupSummaryList"]
    """<p>An array of structures that contain information about the groups that this canary is associated with.</p>"""
    next_token: NotRequired["capo_synthetics.types.pagination_token.PaginationToken"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>ListAssociatedGroups</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_synthetics.types.group_summary_list

        out["Groups"] = capo_synthetics.types.group_summary_list.serialize_json(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedGroupsResponse:
    out: ListAssociatedGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import capo_synthetics.types.group_summary_list

        out["groups"] = capo_synthetics.types.group_summary_list.deserialize_json(
            data["Groups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
