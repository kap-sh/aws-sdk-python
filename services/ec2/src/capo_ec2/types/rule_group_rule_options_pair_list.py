"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupRuleOptionsPairList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.rule_group_rule_options_pair

RuleGroupRuleOptionsPairList: TypeAlias = list[
    "capo_ec2.types.rule_group_rule_options_pair.RuleGroupRuleOptionsPair"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleGroupRuleOptionsPairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.rule_group_rule_options_pair

        capo_ec2.types.rule_group_rule_options_pair.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RuleGroupRuleOptionsPairList:
    import capo_ec2.types.rule_group_rule_options_pair

    out: RuleGroupRuleOptionsPairList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.rule_group_rule_options_pair.deserialize_ec2_query(child)
        )
    return out
