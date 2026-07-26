"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListIdentityProvidersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.max_results
    import capo_workspaces_web.types.pagination_token


class ListIdentityProvidersRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["capo_workspaces_web.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the next page.</p>"""
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityProvidersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdentityProvidersRequest:
    out: ListIdentityProvidersRequest = {}  # type: ignore[typeddict-item]
    return out
