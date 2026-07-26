"""Generated from Smithy shape ``com.amazonaws.waf#CreateRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.rule


class CreateRuleResponse(TypedDict, closed=True):
    rule: NotRequired["capo_waf.types.rule.Rule"]
    """<p>The <a>Rule</a> returned in the <code>CreateRule</code> response.</p>"""
    change_token: NotRequired["capo_waf.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRule</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleResponse) -> dict:
    out: dict = {}
    if "rule" in value:
        import capo_waf.types.rule

        out["Rule"] = capo_waf.types.rule.serialize_aws_json_1_1(value["rule"])
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleResponse:
    out: CreateRuleResponse = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import capo_waf.types.rule

        out["rule"] = capo_waf.types.rule.deserialize_aws_json_1_1(data["Rule"])
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
