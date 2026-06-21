"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ContactCenterSystemType``."""

from typing import Literal, TypeAlias, cast

ContactCenterSystemType: TypeAlias = Literal[
    "GENESYS_ENGAGE_ON_PREMISES",
    "AVAYA_AURA_CALL_CENTER_ELITE",
    "AVAYA_AURA_CONTACT_CENTER",
    "CISCO_UNIFIED_CONTACT_CENTER_ENTERPRISE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactCenterSystemType) -> str:
    return value


def deserialize_json(data: str) -> ContactCenterSystemType:
    return cast(ContactCenterSystemType, data)
