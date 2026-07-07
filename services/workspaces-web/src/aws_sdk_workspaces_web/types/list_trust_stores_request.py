"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListTrustStoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.max_results
    import aws_sdk_workspaces_web.types.pagination_token


class ListTrustStoresRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["aws_sdk_workspaces_web.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrustStoresRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTrustStoresRequest:
    out: ListTrustStoresRequest = {}  # type: ignore[typeddict-item]
    return out
