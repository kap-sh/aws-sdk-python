"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListDeliverabilityTestReportsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.max_items
    import aws_sdk_pinpoint_email.types.next_token


class ListDeliverabilityTestReportsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_pinpoint_email.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListDeliverabilityTestReports</code> to indicate the position in the list of predictive inbox placement tests.</p>"""
    page_size: NotRequired["aws_sdk_pinpoint_email.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListDeliverabilityTestReports</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeliverabilityTestReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeliverabilityTestReportsRequest:
    out: ListDeliverabilityTestReportsRequest = {}  # type: ignore[typeddict-item]
    return out
