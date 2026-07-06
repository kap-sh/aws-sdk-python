"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_rule


class CreateSipRuleResponse(TypedDict, closed=True):
    sip_rule: NotRequired["aws_sdk_chime_sdk_voice.types.sip_rule.SipRule"]
    """<p>The SIP rule information, including the rule ID, triggers, and target applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipRuleResponse) -> dict:
    out: dict = {}
    if "sip_rule" in value:
        import aws_sdk_chime_sdk_voice.types.sip_rule

        out["SipRule"] = aws_sdk_chime_sdk_voice.types.sip_rule.serialize_json(
            value["sip_rule"]
        )
    return out


def deserialize_json(data: dict) -> CreateSipRuleResponse:
    out: CreateSipRuleResponse = {}  # type: ignore[typeddict-item]
    if "SipRule" in data:
        import aws_sdk_chime_sdk_voice.types.sip_rule

        out["sip_rule"] = aws_sdk_chime_sdk_voice.types.sip_rule.deserialize_json(
            data["SipRule"]
        )
    return out
