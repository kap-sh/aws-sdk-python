"""Generated from Smithy shape ``com.amazonaws.sesv2#ListEmailTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.max_items
    import capo_sesv2.types.next_token


class ListEmailTemplatesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListEmailTemplates</code> to indicate the position in the list of email templates.</p>"""
    page_size: NotRequired["capo_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListEmailTemplates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEmailTemplatesRequest:
    out: ListEmailTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
