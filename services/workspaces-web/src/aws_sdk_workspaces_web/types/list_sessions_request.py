"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.max_results
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.portal_id
    import aws_sdk_workspaces_web.types.session_id
    import aws_sdk_workspaces_web.types.session_sort_by
    import aws_sdk_workspaces_web.types.session_status
    import aws_sdk_workspaces_web.types.username


class ListSessionsRequest(TypedDict, closed=True):
    portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId"
    """<p>The ID of the web portal for the sessions.</p>"""
    username: NotRequired["aws_sdk_workspaces_web.types.username.Username"]
    """<p>The username of the session.</p>"""
    session_id: NotRequired["aws_sdk_workspaces_web.types.session_id.SessionId"]
    """<p>The ID of the session.</p>"""
    sort_by: NotRequired["aws_sdk_workspaces_web.types.session_sort_by.SessionSortBy"]
    """<p>The method in which the returned sessions should be sorted.</p>"""
    status: NotRequired["aws_sdk_workspaces_web.types.session_status.SessionStatus"]
    """<p>The status of the session.</p>"""
    max_results: NotRequired["aws_sdk_workspaces_web.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the next page.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSessionsRequest:
    out: ListSessionsRequest = {}  # type: ignore[typeddict-item]
    return out
