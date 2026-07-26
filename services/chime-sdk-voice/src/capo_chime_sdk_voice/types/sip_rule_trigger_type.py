"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipRuleTriggerType``."""

from typing import Literal, TypeAlias, cast

SipRuleTriggerType: TypeAlias = Literal[
    "ToPhoneNumber",
    "RequestUriHostname",
]


# --- restJson1 ser/de ---
def serialize_json(value: SipRuleTriggerType) -> str:
    return value


def deserialize_json(data: str) -> SipRuleTriggerType:
    return cast(SipRuleTriggerType, data)
