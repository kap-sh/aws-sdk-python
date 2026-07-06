"""Generated from Smithy shape ``com.amazonaws.iot#ListThingsInBillingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.billing_group_name
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.registry_max_results


class ListThingsInBillingGroupRequest(TypedDict, closed=True):
    billing_group_name: "aws_sdk_iot.types.billing_group_name.BillingGroupName"
    """<p>The name of the billing group.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.registry_max_results.RegistryMaxResults"
    ]
    """<p>The maximum number of results to return per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingsInBillingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingsInBillingGroupRequest:
    out: ListThingsInBillingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
