"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_rule

SipRuleList: TypeAlias = list["capo_chime_sdk_voice.types.sip_rule.SipRule"]


# --- restJson1 ser/de ---
def serialize_json(value: SipRuleList) -> list:
    import capo_chime_sdk_voice.types.sip_rule

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.sip_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> SipRuleList:
    import capo_chime_sdk_voice.types.sip_rule

    out: SipRuleList = []
    for item in data:
        out.append(capo_chime_sdk_voice.types.sip_rule.deserialize_json(item))
    return out
