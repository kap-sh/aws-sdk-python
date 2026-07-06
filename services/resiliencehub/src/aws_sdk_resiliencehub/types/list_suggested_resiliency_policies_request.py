"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListSuggestedResiliencyPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.max_results
    import aws_sdk_resiliencehub.types.next_token


class ListSuggestedResiliencyPoliciesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuggestedResiliencyPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSuggestedResiliencyPoliciesRequest:
    out: ListSuggestedResiliencyPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
