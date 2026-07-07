"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListResiliencyPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.max_results
    import aws_sdk_resiliencehub.types.next_token


class ListResiliencyPoliciesRequest(TypedDict, closed=True):
    policy_name: NotRequired["aws_sdk_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the resiliency policy.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResiliencyPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResiliencyPoliciesRequest:
    out: ListResiliencyPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
