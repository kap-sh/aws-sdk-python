"""Generated from Smithy shape ``com.amazonaws.ec2#IpamOrganizationalUnitExclusionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_organizational_unit_exclusion

IpamOrganizationalUnitExclusionSet: TypeAlias = list[
    "capo_ec2.types.ipam_organizational_unit_exclusion.IpamOrganizationalUnitExclusion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamOrganizationalUnitExclusionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_organizational_unit_exclusion

        capo_ec2.types.ipam_organizational_unit_exclusion.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> IpamOrganizationalUnitExclusionSet:
    import capo_ec2.types.ipam_organizational_unit_exclusion

    out: IpamOrganizationalUnitExclusionSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_organizational_unit_exclusion.deserialize_ec2_query(
                child
            )
        )
    return out
