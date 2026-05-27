"""Generated from Smithy shape ``com.amazonaws.eks#ListEksAnywhereSubscriptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.eks_anywhere_subscription_status_values
    import aws_sdk_eks.types.list_eks_anywhere_subscriptions_request_max_results
    import aws_sdk_eks.types.string


class ListEksAnywhereSubscriptionsRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_eks.types.list_eks_anywhere_subscriptions_request_max_results.ListEksAnywhereSubscriptionsRequestMaxResults"
    ]
    """<p>The maximum number of cluster results returned by ListEksAnywhereSubscriptions in paginated output. When you use this parameter, ListEksAnywhereSubscriptions returns only maxResults results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListEksAnywhereSubscriptions request with the returned nextToken value. This value can be between 1 and 100. If you don't use this parameter, ListEksAnywhereSubscriptions returns up to 10 results and a nextToken value if applicable.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListEksAnywhereSubscriptions</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>"""
    include_status: NotRequired[
        "aws_sdk_eks.types.eks_anywhere_subscription_status_values.EksAnywhereSubscriptionStatusValues"
    ]
    """<p>An array of subscription statuses to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEksAnywhereSubscriptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEksAnywhereSubscriptionsRequest:
    out: ListEksAnywhereSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    return out
