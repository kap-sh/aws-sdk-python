"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyAllocationRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_allocation_rule

IpamPolicyAllocationRuleList: TypeAlias = list[
    "capo_ec2.types.ipam_policy_allocation_rule.IpamPolicyAllocationRule"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyAllocationRuleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_policy_allocation_rule

        capo_ec2.types.ipam_policy_allocation_rule.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPolicyAllocationRuleList:
    import capo_ec2.types.ipam_policy_allocation_rule

    out: IpamPolicyAllocationRuleList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_policy_allocation_rule.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPolicyAllocationRuleList:
    import capo_ec2.types.ipam_policy_allocation_rule

    out: IpamPolicyAllocationRuleList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_policy_allocation_rule.deserialize_ec2_query(child)
        )
    return out
