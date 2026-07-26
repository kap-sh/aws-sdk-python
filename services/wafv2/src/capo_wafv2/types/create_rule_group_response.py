"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.rule_group_summary


class CreateRuleGroupResponse(TypedDict, closed=True):
    summary: NotRequired["capo_wafv2.types.rule_group_summary.RuleGroupSummary"]
    """<p>High-level information about a <a>RuleGroup</a>, returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a <code>RuleGroup</code>, and the ARN, that you provide to the <a>RuleGroupReferenceStatement</a> to use the rule group in a <a>Rule</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleGroupResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import capo_wafv2.types.rule_group_summary

        out["Summary"] = capo_wafv2.types.rule_group_summary.serialize_aws_json_1_1(
            value["summary"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleGroupResponse:
    out: CreateRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import capo_wafv2.types.rule_group_summary

        out["summary"] = capo_wafv2.types.rule_group_summary.deserialize_aws_json_1_1(
            data["Summary"]
        )
    return out
