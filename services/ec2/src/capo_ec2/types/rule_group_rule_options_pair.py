"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupRuleOptionsPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.resource_arn
    import capo_ec2.types.rule_option_list


class RuleGroupRuleOptionsPair(TypedDict, closed=True):
    rule_group_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the rule group.</p>"""
    rule_options: NotRequired["capo_ec2.types.rule_option_list.RuleOptionList"]
    """<p>The rule options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleGroupRuleOptionsPair, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_group_arn" in value:
        pairs.append((f"{prefix}.RuleGroupArn", str(value["rule_group_arn"])))
    if "rule_options" in value:
        import capo_ec2.types.rule_option_list

        capo_ec2.types.rule_option_list.serialize_ec2_query(
            value["rule_options"], pairs, f"{prefix}.RuleOptionSet"
        )


def deserialize_ec2_query(el: Element) -> RuleGroupRuleOptionsPair:
    out: RuleGroupRuleOptionsPair = {}  # type: ignore[typeddict-item]
    child_rule_group_arn = el.find("RuleGroupArn")
    if child_rule_group_arn is not None:
        out["rule_group_arn"] = str(child_rule_group_arn.text or "")
    if el.find("RuleOptionSet") is not None:
        import capo_ec2.types.rule_option_list

        out["rule_options"] = capo_ec2.types.rule_option_list.deserialize_ec2_query(
            el, "RuleOptionSet"
        )
    return out
