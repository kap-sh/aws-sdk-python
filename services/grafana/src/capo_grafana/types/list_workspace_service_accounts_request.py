"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspaceServiceAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.pagination_token
    import capo_grafana.types.workspace_id


class ListWorkspaceServiceAccountsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of service accounts to include in the results.</p>"""
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccounts</code> operation.)</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The workspace for which to list service accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceServiceAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkspaceServiceAccountsRequest:
    out: ListWorkspaceServiceAccountsRequest = {}  # type: ignore[typeddict-item]
    return out
