"""Generated from Smithy shape ``com.amazonaws.connect#ListUserHierarchyGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_summary_list
    import aws_sdk_connect.types.next_token


class ListUserHierarchyGroupsResponse(TypedDict):
    user_hierarchy_group_summary_list: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_summary_list.HierarchyGroupSummaryList"
    ]
    """<p>Information about the hierarchy groups.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserHierarchyGroupsResponse) -> dict:
    out: dict = {}
    if "user_hierarchy_group_summary_list" in value:
        import aws_sdk_connect.types.hierarchy_group_summary_list

        out["UserHierarchyGroupSummaryList"] = (
            aws_sdk_connect.types.hierarchy_group_summary_list.serialize_json(
                value["user_hierarchy_group_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserHierarchyGroupsResponse:
    out: ListUserHierarchyGroupsResponse = {}  # type: ignore[typeddict-item]
    if "UserHierarchyGroupSummaryList" in data:
        import aws_sdk_connect.types.hierarchy_group_summary_list

        out["user_hierarchy_group_summary_list"] = (
            aws_sdk_connect.types.hierarchy_group_summary_list.deserialize_json(
                data["UserHierarchyGroupSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
