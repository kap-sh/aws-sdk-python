"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.rule_action


class RuleSummary(TypedDict, closed=True):
    name: NotRequired["capo_wafv2.types.entity_name.EntityName"]
    """<p>The name of the rule. </p>"""
    action: NotRequired["capo_wafv2.types.rule_action.RuleAction"]
    """<p>The action that WAF should take on a web request when it matches a rule's statement. Settings at the web ACL level can override the rule action setting. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "action" in value:
        import capo_wafv2.types.rule_action

        out["Action"] = capo_wafv2.types.rule_action.serialize_aws_json_1_1(
            value["action"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Action" in data:
        import capo_wafv2.types.rule_action

        out["action"] = capo_wafv2.types.rule_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    return out
