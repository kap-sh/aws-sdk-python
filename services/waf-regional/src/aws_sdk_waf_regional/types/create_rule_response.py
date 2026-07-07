"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.rule


class CreateRuleResponse(TypedDict, closed=True):
    rule: NotRequired["aws_sdk_waf_regional.types.rule.Rule"]
    """<p>The <a>Rule</a> returned in the <code>CreateRule</code> response.</p>"""
    change_token: NotRequired["aws_sdk_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRule</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleResponse) -> dict:
    out: dict = {}
    if "rule" in value:
        import aws_sdk_waf_regional.types.rule

        out["Rule"] = aws_sdk_waf_regional.types.rule.serialize_aws_json_1_1(
            value["rule"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleResponse:
    out: CreateRuleResponse = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import aws_sdk_waf_regional.types.rule

        out["rule"] = aws_sdk_waf_regional.types.rule.deserialize_aws_json_1_1(
            data["Rule"]
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
