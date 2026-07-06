"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppFlowsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.max_results
    import aws_sdk_socialmessaging.types.next_token


class ListWhatsAppFlowsInput(TypedDict, closed=True):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to list Flows for.</p>"""
    next_token: NotRequired["aws_sdk_socialmessaging.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_socialmessaging.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppFlowsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWhatsAppFlowsInput:
    out: ListWhatsAppFlowsInput = {}  # type: ignore[typeddict-item]
    return out
