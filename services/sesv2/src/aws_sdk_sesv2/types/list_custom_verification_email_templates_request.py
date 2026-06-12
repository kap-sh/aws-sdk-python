"""Generated from Smithy shape ``com.amazonaws.sesv2#ListCustomVerificationEmailTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token


class ListCustomVerificationEmailTemplatesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListCustomVerificationEmailTemplates</code> to indicate the position in the list of custom verification email templates.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListCustomVerificationEmailTemplates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomVerificationEmailTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomVerificationEmailTemplatesRequest:
    out: ListCustomVerificationEmailTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
