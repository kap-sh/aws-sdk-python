"""Generated from Smithy shape ``com.amazonaws.connect#InstanceAttributeType``."""

from typing import Literal, TypeAlias, cast

InstanceAttributeType: TypeAlias = Literal[
    "INBOUND_CALLS",
    "OUTBOUND_CALLS",
    "CONTACTFLOW_LOGS",
    "CONTACT_LENS",
    "AUTO_RESOLVE_BEST_VOICES",
    "USE_CUSTOM_TTS_VOICES",
    "EARLY_MEDIA",
    "MULTI_PARTY_CONFERENCE",
    "HIGH_VOLUME_OUTBOUND",
    "ENHANCED_CONTACT_MONITORING",
    "ENHANCED_CHAT_MONITORING",
    "MULTI_PARTY_CHAT_CONFERENCE",
    "MESSAGE_STREAMING",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceAttributeType) -> str:
    return value


def deserialize_json(data: str) -> InstanceAttributeType:
    return cast(InstanceAttributeType, data)
