"""Generated from Smithy shape ``com.amazonaws.iot#ListBillingGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.billing_group_name
    import capo_iot.types.next_token
    import capo_iot.types.registry_max_results


class ListBillingGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["capo_iot.types.registry_max_results.RegistryMaxResults"]
    """<p>The maximum number of results to return per request.</p>"""
    name_prefix_filter: NotRequired[
        "capo_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>Limit the results to billing groups whose names have the given prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBillingGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBillingGroupsRequest:
    out: ListBillingGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
