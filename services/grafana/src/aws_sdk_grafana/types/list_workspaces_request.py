"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspacesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_grafana.types.pagination_token


class ListWorkspacesRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of workspaces to include in the results.</p>"""
    next_token: NotRequired["aws_sdk_grafana.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of workspaces to return. (You receive this token from a previous <code>ListWorkspaces</code> operation.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkspacesRequest:
    out: ListWorkspacesRequest = {}  # type: ignore[typeddict-item]
    return out
