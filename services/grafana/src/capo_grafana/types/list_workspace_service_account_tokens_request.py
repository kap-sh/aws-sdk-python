"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspaceServiceAccountTokensRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.pagination_token
    import capo_grafana.types.workspace_id


class ListWorkspaceServiceAccountTokensRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of tokens to include in the results.</p>"""
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccountTokens</code> operation.)</p>"""
    service_account_id: "str"
    """<p>The ID of the service account for which to return tokens.</p>"""
    workspace_id: "capo_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace for which to return tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceServiceAccountTokensRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkspaceServiceAccountTokensRequest:
    out: ListWorkspaceServiceAccountTokensRequest = {}  # type: ignore[typeddict-item]
    return out
