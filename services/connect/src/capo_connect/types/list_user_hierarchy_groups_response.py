"""Generated from Smithy shape ``com.amazonaws.connect#ListUserHierarchyGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_summary_list
    import capo_connect.types.next_token


class ListUserHierarchyGroupsResponse(TypedDict, closed=True):
    user_hierarchy_group_summary_list: NotRequired[
        "capo_connect.types.hierarchy_group_summary_list.HierarchyGroupSummaryList"
    ]
    """<p>Information about the hierarchy groups.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserHierarchyGroupsResponse) -> dict:
    out: dict = {}
    if "user_hierarchy_group_summary_list" in value:
        import capo_connect.types.hierarchy_group_summary_list

        out["UserHierarchyGroupSummaryList"] = (
            capo_connect.types.hierarchy_group_summary_list.serialize_json(
                value["user_hierarchy_group_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserHierarchyGroupsResponse:
    out: ListUserHierarchyGroupsResponse = {}  # type: ignore[typeddict-item]
    if "UserHierarchyGroupSummaryList" in data:
        import capo_connect.types.hierarchy_group_summary_list

        out["user_hierarchy_group_summary_list"] = (
            capo_connect.types.hierarchy_group_summary_list.deserialize_json(
                data["UserHierarchyGroupSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
