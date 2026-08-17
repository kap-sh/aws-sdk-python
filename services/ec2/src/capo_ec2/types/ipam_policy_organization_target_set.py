"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyOrganizationTargetSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_organization_target

IpamPolicyOrganizationTargetSet: TypeAlias = list[
    "capo_ec2.types.ipam_policy_organization_target.IpamPolicyOrganizationTarget"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyOrganizationTargetSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_policy_organization_target

        capo_ec2.types.ipam_policy_organization_target.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamPolicyOrganizationTargetSet:
    import capo_ec2.types.ipam_policy_organization_target

    out: IpamPolicyOrganizationTargetSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_policy_organization_target.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamPolicyOrganizationTargetSet:
    import capo_ec2.types.ipam_policy_organization_target

    out: IpamPolicyOrganizationTargetSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_policy_organization_target.deserialize_ec2_query(child)
        )
    return out
