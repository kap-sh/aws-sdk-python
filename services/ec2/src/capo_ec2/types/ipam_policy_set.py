"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy

IpamPolicySet: TypeAlias = list["capo_ec2.types.ipam_policy.IpamPolicy"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_policy

        capo_ec2.types.ipam_policy.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPolicySet:
    import capo_ec2.types.ipam_policy

    out: IpamPolicySet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_policy.deserialize_ec2_query(child))
    return out
