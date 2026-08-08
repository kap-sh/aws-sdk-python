"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupTypePair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string


class RuleGroupTypePair(TypedDict, closed=True):
    rule_group_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the rule group.</p>"""
    rule_group_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The rule group type. The possible values are <code>Domain List</code> and <code>Suricata</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleGroupTypePair, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_group_arn" in value:
        pairs.append((f"{key_prefix}RuleGroupArn", str(value["rule_group_arn"])))
    if "rule_group_type" in value:
        pairs.append((f"{key_prefix}RuleGroupType", str(value["rule_group_type"])))


def deserialize_ec2_query(el: Element) -> RuleGroupTypePair:
    out: RuleGroupTypePair = {}  # type: ignore[typeddict-item]
    child_rule_group_arn = el.find("ruleGroupArn")
    if child_rule_group_arn is not None:
        out["rule_group_arn"] = str(child_rule_group_arn.text or "")
    child_rule_group_type = el.find("ruleGroupType")
    if child_rule_group_type is not None:
        out["rule_group_type"] = str(child_rule_group_type.text or "")
    return out
