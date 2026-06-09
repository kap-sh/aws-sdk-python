"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyAllocationRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_allocation_rule

IpamPolicyAllocationRuleList: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_policy_allocation_rule.IpamPolicyAllocationRule"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyAllocationRuleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_policy_allocation_rule

        aws_sdk_ec2.types.ipam_policy_allocation_rule.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPolicyAllocationRuleList:
    import aws_sdk_ec2.types.ipam_policy_allocation_rule

    out: IpamPolicyAllocationRuleList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.ipam_policy_allocation_rule.deserialize_ec2_query(child)
        )
    return out
