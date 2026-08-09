"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleConditionRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request

IpamPrefixListResolverRuleConditionRequestSet: TypeAlias = list[
    "capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request.IpamPrefixListResolverRuleConditionRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRuleConditionRequestSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request

        capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleConditionRequestSet:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request

    out: IpamPrefixListResolverRuleConditionRequestSet = []
    for child in el.findall("Condition"):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPrefixListResolverRuleConditionRequestSet:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request

    out: IpamPrefixListResolverRuleConditionRequestSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_rule_condition_request.deserialize_ec2_query(
                child
            )
        )
    return out
