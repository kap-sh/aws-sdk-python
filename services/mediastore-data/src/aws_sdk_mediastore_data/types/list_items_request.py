"""Generated from Smithy shape ``com.amazonaws.mediastoredata#ListItemsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediastore_data.types.list_limit
    import aws_sdk_mediastore_data.types.list_path_naming
    import aws_sdk_mediastore_data.types.pagination_token


class ListItemsRequest(TypedDict):
    path: NotRequired["aws_sdk_mediastore_data.types.list_path_naming.ListPathNaming"]
    """<p>The path in the container from which to retrieve items. Format: <folder name>/<folder name>/<file name></p>"""
    max_results: NotRequired["aws_sdk_mediastore_data.types.list_limit.ListLimit"]
    """<p>The maximum number of results to return per API request. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) The service might return fewer results than the <code>MaxResults</code> value.</p> <p>If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.</p>"""
    next_token: NotRequired[
        "aws_sdk_mediastore_data.types.pagination_token.PaginationToken"
    ]
    """<p>The token that identifies which batch of results that you want to see. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. The service returns the first batch of results (up to 500) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListItems</code> request a second time and specify the <code>NextToken</code> value.</p> <p>Tokens expire after 15 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListItemsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListItemsRequest:
    out: ListItemsRequest = {}  # type: ignore[typeddict-item]
    return out
