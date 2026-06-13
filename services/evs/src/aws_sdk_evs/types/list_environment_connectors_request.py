"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentConnectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.max_results
    import aws_sdk_evs.types.pagination_token


class ListEnvironmentConnectorsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""
    max_results: NotRequired["aws_sdk_evs.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>"""
    environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentConnectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentConnectorsRequest:
    out: ListEnvironmentConnectorsRequest = {}  # type: ignore[typeddict-item]
    return out
