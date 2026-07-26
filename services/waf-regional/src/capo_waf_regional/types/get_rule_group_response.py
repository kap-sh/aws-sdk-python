"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.rule_group


class GetRuleGroupResponse(TypedDict, closed=True):
    rule_group: NotRequired["capo_waf_regional.types.rule_group.RuleGroup"]
    """<p>Information about the <a>RuleGroup</a> that you specified in the <code>GetRuleGroup</code> request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRuleGroupResponse) -> dict:
    out: dict = {}
    if "rule_group" in value:
        import capo_waf_regional.types.rule_group

        out["RuleGroup"] = capo_waf_regional.types.rule_group.serialize_aws_json_1_1(
            value["rule_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRuleGroupResponse:
    out: GetRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "RuleGroup" in data:
        import capo_waf_regional.types.rule_group

        out["rule_group"] = capo_waf_regional.types.rule_group.deserialize_aws_json_1_1(
            data["RuleGroup"]
        )
    return out
