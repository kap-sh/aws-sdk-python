"""Generated from Smithy shape ``com.amazonaws.socialmessaging#PublishWhatsAppFlowInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.meta_flow_id


class PublishWhatsAppFlowInput(TypedDict):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow to publish.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishWhatsAppFlowInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["flowId"] = value["flow_id"]
    return out


def deserialize_json(data: dict) -> PublishWhatsAppFlowInput:
    out: PublishWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PublishWhatsAppFlowInput.id required")
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("PublishWhatsAppFlowInput.flow_id required")
    return out
