"""Generated from Smithy shape ``com.amazonaws.connect#ListFlowAssociationResourceType``."""

from typing import Literal, TypeAlias, cast

ListFlowAssociationResourceType: TypeAlias = Literal[
    "WHATSAPP_MESSAGING_PHONE_NUMBER",
    "VOICE_PHONE_NUMBER",
    "INBOUND_EMAIL",
    "OUTBOUND_EMAIL",
    "ANALYTICS_CONNECTOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowAssociationResourceType) -> str:
    return value


def deserialize_json(data: str) -> ListFlowAssociationResourceType:
    return cast(ListFlowAssociationResourceType, data)
