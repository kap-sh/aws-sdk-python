"""Generated from Smithy shape ``com.amazonaws.grafana#ListVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.pagination_token
    import capo_grafana.types.workspace_id


class ListVersionsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["capo_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of results. You receive this token from a previous <code>ListVersions</code> operation.</p>"""
    workspace_id: NotRequired["capo_grafana.types.workspace_id.WorkspaceId"]
    """<p>The ID of the workspace to list the available upgrade versions. If not included, lists all versions of Grafana that are supported for <code>CreateWorkspace</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVersionsRequest:
    out: ListVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
