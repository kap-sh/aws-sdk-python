"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListSipRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.next_token_string
    import capo_chime_sdk_voice.types.sip_rule_list


class ListSipRulesResponse(TypedDict, closed=True):
    sip_rules: NotRequired["capo_chime_sdk_voice.types.sip_rule_list.SipRuleList"]
    """<p>The list of SIP rules and details.</p>"""
    next_token: NotRequired[
        "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
    ]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSipRulesResponse) -> dict:
    out: dict = {}
    if "sip_rules" in value:
        import capo_chime_sdk_voice.types.sip_rule_list

        out["SipRules"] = capo_chime_sdk_voice.types.sip_rule_list.serialize_json(
            value["sip_rules"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSipRulesResponse:
    out: ListSipRulesResponse = {}  # type: ignore[typeddict-item]
    if "SipRules" in data:
        import capo_chime_sdk_voice.types.sip_rule_list

        out["sip_rules"] = capo_chime_sdk_voice.types.sip_rule_list.deserialize_json(
            data["SipRules"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
