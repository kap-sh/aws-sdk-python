"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentHostsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.max_results
    import aws_sdk_evs.types.pagination_token


class ListEnvironmentHostsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""
    max_results: NotRequired["aws_sdk_evs.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>"""
    environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentHostsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentHostsRequest:
    out: ListEnvironmentHostsRequest = {}  # type: ignore[typeddict-item]
    return out
