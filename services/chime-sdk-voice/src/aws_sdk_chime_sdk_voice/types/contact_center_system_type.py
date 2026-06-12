"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ContactCenterSystemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

ContactCenterSystemType: TypeAlias = Literal[
    "GENESYS_ENGAGE_ON_PREMISES",
    "AVAYA_AURA_CALL_CENTER_ELITE",
    "AVAYA_AURA_CONTACT_CENTER",
    "CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENESYS_ENGAGE_ON_PREMISES",
        "AVAYA_AURA_CALL_CENTER_ELITE",
        "AVAYA_AURA_CONTACT_CENTER",
        "CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE",
    )
)


def serialize_json(value: ContactCenterSystemType) -> str:
    return value


def deserialize_json(data: str) -> ContactCenterSystemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactCenterSystemType value: {data!r}")
    return cast(ContactCenterSystemType, data)
