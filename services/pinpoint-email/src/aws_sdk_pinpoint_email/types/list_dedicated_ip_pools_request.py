"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListDedicatedIpPoolsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.max_items
    import aws_sdk_pinpoint_email.types.next_token


class ListDedicatedIpPoolsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_pinpoint_email.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListDedicatedIpPools</code> to indicate the position in the list of dedicated IP pools.</p>"""
    page_size: NotRequired["aws_sdk_pinpoint_email.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListDedicatedIpPools</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDedicatedIpPoolsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDedicatedIpPoolsRequest:
    out: ListDedicatedIpPoolsRequest = {}  # type: ignore[typeddict-item]
    return out
