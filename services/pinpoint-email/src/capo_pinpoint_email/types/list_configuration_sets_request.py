"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListConfigurationSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.max_items
    import capo_pinpoint_email.types.next_token


class ListConfigurationSetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_pinpoint_email.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListConfigurationSets</code> to indicate the position in the list of configuration sets.</p>"""
    page_size: NotRequired["capo_pinpoint_email.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListConfigurationSets</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationSetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConfigurationSetsRequest:
    out: ListConfigurationSetsRequest = {}  # type: ignore[typeddict-item]
    return out
