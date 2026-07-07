"""Generated from Smithy shape ``com.amazonaws.connect#SearchWorkspaceAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.workspace_association_search_summary_list


class SearchWorkspaceAssociationsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    workspace_associations: NotRequired[
        "aws_sdk_connect.types.workspace_association_search_summary_list.WorkspaceAssociationSearchSummaryList"
    ]
    """<p>A list of workspace associations that match the search criteria.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate total number of workspace associations that match the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchWorkspaceAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "workspace_associations" in value:
        import aws_sdk_connect.types.workspace_association_search_summary_list

        out["WorkspaceAssociations"] = (
            aws_sdk_connect.types.workspace_association_search_summary_list.serialize_json(
                value["workspace_associations"]
            )
        )
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchWorkspaceAssociationsResponse:
    out: SearchWorkspaceAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "WorkspaceAssociations" in data:
        import aws_sdk_connect.types.workspace_association_search_summary_list

        out["workspace_associations"] = (
            aws_sdk_connect.types.workspace_association_search_summary_list.deserialize_json(
                data["WorkspaceAssociations"]
            )
        )
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
