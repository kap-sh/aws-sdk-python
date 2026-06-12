"""Generated from Smithy shape ``com.amazonaws.appsync#ListFunctionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.max_results
    import aws_sdk_appsync.types.pagination_token
    import aws_sdk_appsync.types.string


class ListFunctionsRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The GraphQL API ID.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""
    max_results: "aws_sdk_appsync.types.max_results.MaxResults"
    """<p>The maximum number of results that you want the request to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionsRequest:
    out: ListFunctionsRequest = {}  # type: ignore[typeddict-item]
    return out
