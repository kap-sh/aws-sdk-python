"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListSipRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.next_token_string
    import aws_sdk_chime_sdk_voice.types.sip_rule_list


class ListSipRulesResponse(TypedDict):
    sip_rules: NotRequired["aws_sdk_chime_sdk_voice.types.sip_rule_list.SipRuleList"]
    """<p>The list of SIP rules and details.</p>"""
    next_token: NotRequired[
        "aws_sdk_chime_sdk_voice.types.next_token_string.NextTokenString"
    ]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSipRulesResponse) -> dict:
    out: dict = {}
    if "sip_rules" in value:
        import aws_sdk_chime_sdk_voice.types.sip_rule_list

        out["SipRules"] = aws_sdk_chime_sdk_voice.types.sip_rule_list.serialize_json(
            value["sip_rules"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSipRulesResponse:
    out: ListSipRulesResponse = {}  # type: ignore[typeddict-item]
    if "SipRules" in data:
        import aws_sdk_chime_sdk_voice.types.sip_rule_list

        out["sip_rules"] = aws_sdk_chime_sdk_voice.types.sip_rule_list.deserialize_json(
            data["SipRules"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
