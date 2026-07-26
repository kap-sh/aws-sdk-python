"""Generated from Smithy shape ``com.amazonaws.sesv2#ListSuppressedDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.max_items
    import capo_sesv2.types.next_token
    import capo_sesv2.types.suppression_list_reasons
    import capo_sesv2.types.tenant_name
    import capo_sesv2.types.timestamp


class ListSuppressedDestinationsRequest(TypedDict, closed=True):
    tenant_name: NotRequired["capo_sesv2.types.tenant_name.TenantName"]
    """<p>The name of the tenant whose suppression list you want to retrieve. If you omit this parameter, the operation targets the account-level suppression list.</p>"""
    reasons: NotRequired[
        "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
    ]
    """<p>The factors that caused the email address to be added to the suppression list for your account or for a specific tenant.</p>"""
    start_date: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list after a specific date.</p>"""
    end_date: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list before a specific date.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListSuppressedDestinations</code> to indicate the position in the list of suppressed email addresses.</p>"""
    page_size: NotRequired["capo_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListSuppressedDestinations</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuppressedDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSuppressedDestinationsRequest:
    out: ListSuppressedDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
