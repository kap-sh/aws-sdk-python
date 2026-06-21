"""Generated from Smithy shape ``com.amazonaws.connect#FlowAssociationResourceType``."""

from typing import Literal, TypeAlias, cast

FlowAssociationResourceType: TypeAlias = Literal[
    "SMS_PHONE_NUMBER",
    "INBOUND_EMAIL",
    "OUTBOUND_EMAIL",
    "ANALYTICS_CONNECTOR",
    "WHATSAPP_MESSAGING_PHONE_NUMBER",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowAssociationResourceType) -> str:
    return value


def deserialize_json(data: str) -> FlowAssociationResourceType:
    return cast(FlowAssociationResourceType, data)
