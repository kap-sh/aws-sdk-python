"""Generated from Smithy shape ``com.amazonaws.waf#CreateRateBasedRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.rate_based_rule


class CreateRateBasedRuleResponse(TypedDict, closed=True):
    rule: NotRequired["capo_waf.types.rate_based_rule.RateBasedRule"]
    """<p>The <a>RateBasedRule</a> that is returned in the <code>CreateRateBasedRule</code> response.</p>"""
    change_token: NotRequired["capo_waf.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRateBasedRule</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRateBasedRuleResponse) -> dict:
    out: dict = {}
    if "rule" in value:
        import capo_waf.types.rate_based_rule

        out["Rule"] = capo_waf.types.rate_based_rule.serialize_aws_json_1_1(
            value["rule"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRateBasedRuleResponse:
    out: CreateRateBasedRuleResponse = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import capo_waf.types.rate_based_rule

        out["rule"] = capo_waf.types.rate_based_rule.deserialize_aws_json_1_1(
            data["Rule"]
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
