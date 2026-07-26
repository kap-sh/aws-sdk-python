"""Generated from Smithy shape ``com.amazonaws.connect#SearchUserHierarchyGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.user_hierarchy_group_list


class SearchUserHierarchyGroupsResponse(TypedDict, closed=True):
    user_hierarchy_groups: NotRequired[
        "capo_connect.types.user_hierarchy_group_list.UserHierarchyGroupList"
    ]
    """<p>Information about the userHierarchyGroups.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of userHierarchyGroups which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchUserHierarchyGroupsResponse) -> dict:
    out: dict = {}
    if "user_hierarchy_groups" in value:
        import capo_connect.types.user_hierarchy_group_list

        out["UserHierarchyGroups"] = (
            capo_connect.types.user_hierarchy_group_list.serialize_json(
                value["user_hierarchy_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchUserHierarchyGroupsResponse:
    out: SearchUserHierarchyGroupsResponse = {}  # type: ignore[typeddict-item]
    if "UserHierarchyGroups" in data:
        import capo_connect.types.user_hierarchy_group_list

        out["user_hierarchy_groups"] = (
            capo_connect.types.user_hierarchy_group_list.deserialize_json(
                data["UserHierarchyGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
