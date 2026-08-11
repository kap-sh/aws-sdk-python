"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyAllocationRuleListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_allocation_rule_request

IpamPolicyAllocationRuleListRequest: TypeAlias = list[
    "capo_ec2.types.ipam_policy_allocation_rule_request.IpamPolicyAllocationRuleRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyAllocationRuleListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_policy_allocation_rule_request

        capo_ec2.types.ipam_policy_allocation_rule_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPolicyAllocationRuleListRequest:
    import capo_ec2.types.ipam_policy_allocation_rule_request

    out: IpamPolicyAllocationRuleListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_policy_allocation_rule_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPolicyAllocationRuleListRequest:
    import capo_ec2.types.ipam_policy_allocation_rule_request

    out: IpamPolicyAllocationRuleListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_policy_allocation_rule_request.deserialize_ec2_query(
                child
            )
        )
    return out
