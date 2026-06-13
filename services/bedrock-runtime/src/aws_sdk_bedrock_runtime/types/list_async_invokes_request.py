"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ListAsyncInvokesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.async_invoke_status
    import aws_sdk_bedrock_runtime.types.max_results
    import aws_sdk_bedrock_runtime.types.pagination_token
    import aws_sdk_bedrock_runtime.types.sort_async_invocation_by
    import aws_sdk_bedrock_runtime.types.sort_order
    import aws_sdk_bedrock_runtime.types.timestamp


class ListAsyncInvokesRequest(TypedDict):
    submit_time_after: NotRequired["aws_sdk_bedrock_runtime.types.timestamp.Timestamp"]
    """<p>Include invocations submitted after this time.</p>"""
    submit_time_before: NotRequired["aws_sdk_bedrock_runtime.types.timestamp.Timestamp"]
    """<p>Include invocations submitted before this time.</p>"""
    status_equals: NotRequired[
        "aws_sdk_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus"
    ]
    """<p>Filter invocations by status.</p>"""
    max_results: NotRequired["aws_sdk_bedrock_runtime.types.max_results.MaxResults"]
    """<p>The maximum number of invocations to return in one page of results.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_runtime.types.pagination_token.PaginationToken"
    ]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    sort_by: (
        "aws_sdk_bedrock_runtime.types.sort_async_invocation_by.SortAsyncInvocationBy"
    )
    """<p>How to sort the response.</p>"""
    sort_order: "aws_sdk_bedrock_runtime.types.sort_order.SortOrder"
    """<p>The sorting order for the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAsyncInvokesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAsyncInvokesRequest:
    out: ListAsyncInvokesRequest = {}  # type: ignore[typeddict-item]
    return out
