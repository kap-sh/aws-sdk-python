"""Generated from Smithy shape ``com.amazonaws.synthetics#ListAssociatedGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.group_summary_list
    import aws_sdk_synthetics.types.pagination_token


class ListAssociatedGroupsResponse(TypedDict):
    groups: NotRequired["aws_sdk_synthetics.types.group_summary_list.GroupSummaryList"]
    """<p>An array of structures that contain information about the groups that this canary is associated with.</p>"""
    next_token: NotRequired["aws_sdk_synthetics.types.pagination_token.PaginationToken"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>ListAssociatedGroups</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_synthetics.types.group_summary_list

        out["Groups"] = aws_sdk_synthetics.types.group_summary_list.serialize_json(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedGroupsResponse:
    out: ListAssociatedGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_synthetics.types.group_summary_list

        out["groups"] = aws_sdk_synthetics.types.group_summary_list.deserialize_json(
            data["Groups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
