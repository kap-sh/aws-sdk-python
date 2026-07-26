"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetSipRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sip_rule


class GetSipRuleResponse(TypedDict, closed=True):
    sip_rule: NotRequired["capo_chime_sdk_voice.types.sip_rule.SipRule"]
    """<p>The SIP rule details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSipRuleResponse) -> dict:
    out: dict = {}
    if "sip_rule" in value:
        import capo_chime_sdk_voice.types.sip_rule

        out["SipRule"] = capo_chime_sdk_voice.types.sip_rule.serialize_json(
            value["sip_rule"]
        )
    return out


def deserialize_json(data: dict) -> GetSipRuleResponse:
    out: GetSipRuleResponse = {}  # type: ignore[typeddict-item]
    if "SipRule" in data:
        import capo_chime_sdk_voice.types.sip_rule

        out["sip_rule"] = capo_chime_sdk_voice.types.sip_rule.deserialize_json(
            data["SipRule"]
        )
    return out
