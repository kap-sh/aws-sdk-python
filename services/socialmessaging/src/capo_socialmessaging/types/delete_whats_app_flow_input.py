"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DeleteWhatsAppFlowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_flow_id


class DeleteWhatsAppFlowInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "capo_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWhatsAppFlowInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWhatsAppFlowInput:
    out: DeleteWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
    return out
