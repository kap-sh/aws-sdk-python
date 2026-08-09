"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_request

IpamPrefixListResolverRuleRequestSet: TypeAlias = list[
    "capo_ec2.types.ipam_prefix_list_resolver_rule_request.IpamPrefixListResolverRuleRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRuleRequestSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_prefix_list_resolver_rule_request

        capo_ec2.types.ipam_prefix_list_resolver_rule_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleRequestSet:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_request

    out: IpamPrefixListResolverRuleRequestSet = []
    for child in el.findall("Rule"):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_rule_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPrefixListResolverRuleRequestSet:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_request

    out: IpamPrefixListResolverRuleRequestSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_prefix_list_resolver_rule_request.deserialize_ec2_query(
                child
            )
        )
    return out
