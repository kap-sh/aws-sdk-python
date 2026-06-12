"""Generated from Smithy shape ``com.amazonaws.waf#CreateRateBasedRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.rate_based_rule


class CreateRateBasedRuleResponse(TypedDict):
    rule: NotRequired["aws_sdk_waf.types.rate_based_rule.RateBasedRule"]
    """<p>The <a>RateBasedRule</a> that is returned in the <code>CreateRateBasedRule</code> response.</p>"""
    change_token: NotRequired["aws_sdk_waf.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRateBasedRule</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRateBasedRuleResponse) -> dict:
    out: dict = {}
    if "rule" in value:
        import aws_sdk_waf.types.rate_based_rule

        out["Rule"] = aws_sdk_waf.types.rate_based_rule.serialize_aws_json_1_1(
            value["rule"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRateBasedRuleResponse:
    out: CreateRateBasedRuleResponse = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import aws_sdk_waf.types.rate_based_rule

        out["rule"] = aws_sdk_waf.types.rate_based_rule.deserialize_aws_json_1_1(
            data["Rule"]
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
