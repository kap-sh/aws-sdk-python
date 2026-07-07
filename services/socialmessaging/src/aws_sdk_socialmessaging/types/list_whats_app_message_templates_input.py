"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppMessageTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.max_results
    import aws_sdk_socialmessaging.types.next_token


class ListWhatsAppMessageTemplatesInput(TypedDict, closed=True):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to list templates for.</p>"""
    next_token: NotRequired["aws_sdk_socialmessaging.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_socialmessaging.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page (1-100).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppMessageTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWhatsAppMessageTemplatesInput:
    out: ListWhatsAppMessageTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
