"""Generated from Smithy shape ``com.amazonaws.connect#InstanceAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: InstanceAttributeType) -> str:
    return value


def deserialize_json(data: str) -> InstanceAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceAttributeType value: {data!r}")
    return cast(InstanceAttributeType, data)
