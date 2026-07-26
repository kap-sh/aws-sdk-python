"""Generated from Smithy shape ``com.amazonaws.connect#SearchWorkspacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token
    import capo_connect.types.workspace_search_summary_list


class SearchWorkspacesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    workspaces: NotRequired[
        "capo_connect.types.workspace_search_summary_list.WorkspaceSearchSummaryList"
    ]
    """<p>A list of workspaces that match the search criteria.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate total number of workspaces that match the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchWorkspacesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "workspaces" in value:
        import capo_connect.types.workspace_search_summary_list

        out["Workspaces"] = (
            capo_connect.types.workspace_search_summary_list.serialize_json(
                value["workspaces"]
            )
        )
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchWorkspacesResponse:
    out: SearchWorkspacesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Workspaces" in data:
        import capo_connect.types.workspace_search_summary_list

        out["workspaces"] = (
            capo_connect.types.workspace_search_summary_list.deserialize_json(
                data["Workspaces"]
            )
        )
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
