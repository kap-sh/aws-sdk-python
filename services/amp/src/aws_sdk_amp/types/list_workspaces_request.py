"""Generated from Smithy shape ``com.amazonaws.amp#ListWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.pagination_token
    import aws_sdk_amp.types.workspace_alias


class ListWorkspacesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_amp.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.</p> <p>For example, if your initial request has <code>maxResults</code> of 10, and there are 12 workspaces to return, then your initial request will return 10 and a <code>nextToken</code>. Using the next token in a subsequent call will return the remaining 2 workspaces.</p>"""
    alias: NotRequired["aws_sdk_amp.types.workspace_alias.WorkspaceAlias"]
    """<p>If this is included, it filters the results to only the workspaces with names that start with the value that you specify here.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of workspaces to return per request. The default is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspacesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWorkspacesRequest:
    out: ListWorkspacesRequest = {}  # type: ignore[typeddict-item]
    return out
