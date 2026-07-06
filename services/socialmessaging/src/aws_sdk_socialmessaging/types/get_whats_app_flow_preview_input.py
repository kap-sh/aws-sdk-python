"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppFlowPreviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.meta_flow_id


class GetWhatsAppFlowPreviewInput(TypedDict, closed=True):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow to preview.</p>"""
    invalidate: NotRequired["bool"]
    """<p>Set to <code>true</code> to force generation of a new preview URL. Use this if the previous URL has been compromised or you want a fresh expiration period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppFlowPreviewInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWhatsAppFlowPreviewInput:
    out: GetWhatsAppFlowPreviewInput = {}  # type: ignore[typeddict-item]
    return out
