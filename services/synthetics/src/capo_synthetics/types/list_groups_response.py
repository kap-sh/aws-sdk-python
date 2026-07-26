"""Generated from Smithy shape ``com.amazonaws.synthetics#ListGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.group_summary_list
    import capo_synthetics.types.token


class ListGroupsResponse(TypedDict, closed=True):
    groups: NotRequired["capo_synthetics.types.group_summary_list.GroupSummaryList"]
    """<p>An array of structures that each contain information about one group.</p>"""
    next_token: NotRequired["capo_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>ListGroups</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_synthetics.types.group_summary_list

        out["Groups"] = capo_synthetics.types.group_summary_list.serialize_json(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupsResponse:
    out: ListGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import capo_synthetics.types.group_summary_list

        out["groups"] = capo_synthetics.types.group_summary_list.deserialize_json(
            data["Groups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
