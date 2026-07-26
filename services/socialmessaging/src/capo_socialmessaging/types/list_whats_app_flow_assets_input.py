"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppFlowAssetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.max_results
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.next_token


class ListWhatsAppFlowAssetsInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow whose assets to list.</p>"""
    next_token: NotRequired["capo_socialmessaging.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_socialmessaging.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppFlowAssetsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWhatsAppFlowAssetsInput:
    out: ListWhatsAppFlowAssetsInput = {}  # type: ignore[typeddict-item]
    return out
