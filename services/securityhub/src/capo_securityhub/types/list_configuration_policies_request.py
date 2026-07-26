"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConfigurationPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token


class ListConfigurationPoliciesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p> The NextToken value that's returned from a previous paginated <code>ListConfigurationPolicies</code> request where <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return. </p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p> The maximum number of results that's returned by <code>ListConfigurationPolicies</code> in each page of the response. When this parameter is used, <code>ListConfigurationPolicies</code> returns the specified number of results in a single page and a <code>NextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListConfigurationPolicies</code> request with the returned <code>NextToken</code> value. A valid range for <code>MaxResults</code> is between 1 and 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConfigurationPoliciesRequest:
    out: ListConfigurationPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
