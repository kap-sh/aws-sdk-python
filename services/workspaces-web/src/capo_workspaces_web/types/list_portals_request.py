"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListPortalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.max_results
    import capo_workspaces_web.types.pagination_token


class ListPortalsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation. </p>"""
    max_results: NotRequired["capo_workspaces_web.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPortalsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPortalsRequest:
    out: ListPortalsRequest = {}  # type: ignore[typeddict-item]
    return out
