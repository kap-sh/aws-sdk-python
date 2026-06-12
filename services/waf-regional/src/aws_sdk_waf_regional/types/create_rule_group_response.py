"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateRuleGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.rule_group


class CreateRuleGroupResponse(TypedDict):
    rule_group: NotRequired["aws_sdk_waf_regional.types.rule_group.RuleGroup"]
    """<p>An empty <a>RuleGroup</a>.</p>"""
    change_token: NotRequired["aws_sdk_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRuleGroup</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleGroupResponse) -> dict:
    out: dict = {}
    if "rule_group" in value:
        import aws_sdk_waf_regional.types.rule_group

        out["RuleGroup"] = aws_sdk_waf_regional.types.rule_group.serialize_aws_json_1_1(
            value["rule_group"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleGroupResponse:
    out: CreateRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "RuleGroup" in data:
        import aws_sdk_waf_regional.types.rule_group

        out["rule_group"] = (
            aws_sdk_waf_regional.types.rule_group.deserialize_aws_json_1_1(
                data["RuleGroup"]
            )
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
