"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowHealthEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_health_entity_type
    import capo_socialmessaging.types.meta_flow_health_status_availability


class MetaFlowHealthEntity(TypedDict, closed=True):
    entity_type: "capo_socialmessaging.types.meta_flow_health_entity_type.MetaFlowHealthEntityType"
    """<p>The type of entity (for example, FLOW, WABA, BUSINESS, or APP).</p>"""
    id: "str"
    """<p>The unique identifier of the entity.</p>"""
    can_send_message: "capo_socialmessaging.types.meta_flow_health_status_availability.MetaFlowHealthStatusAvailability"
    """<p>The messaging availability status for this entity (for example, AVAILABLE, LIMITED, or BLOCKED).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowHealthEntity) -> dict:
    out: dict = {}
    out["entityType"] = value["entity_type"]
    out["id"] = value["id"]
    out["canSendMessage"] = value["can_send_message"]
    return out


def deserialize_json(data: dict) -> MetaFlowHealthEntity:
    out: MetaFlowHealthEntity = {}  # type: ignore[typeddict-item]
    if "entityType" in data:
        out["entity_type"] = data["entityType"]
    else:
        raise DeserializationError("MetaFlowHealthEntity.entity_type required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("MetaFlowHealthEntity.id required")
    if "canSendMessage" in data:
        out["can_send_message"] = data["canSendMessage"]
    else:
        raise DeserializationError("MetaFlowHealthEntity.can_send_message required")
    return out
