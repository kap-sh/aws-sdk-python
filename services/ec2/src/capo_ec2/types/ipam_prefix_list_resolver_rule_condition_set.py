"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleConditionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition

IpamPrefixListResolverRuleConditionSet: TypeAlias = list[
    "capo_ec2.types.ipam_prefix_list_resolver_rule_condition.IpamPrefixListResolverRuleCondition"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRuleConditionSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_prefix_list_resolver_rule_condition

        capo_ec2.types.ipam_prefix_list_resolver_rule_condition.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleConditionSet:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition

    out: IpamPrefixListResolverRuleConditionSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_rule_condition.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPrefixListResolverRuleConditionSet:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition

    out: IpamPrefixListResolverRuleConditionSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_rule_condition.deserialize_ec2_query(
                child
            )
        )
    return out
