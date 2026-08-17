"""Generated from Smithy shape ``com.amazonaws.ec2#AddIpamOrganizationalUnitExclusionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.add_ipam_organizational_unit_exclusion

AddIpamOrganizationalUnitExclusionSet: TypeAlias = list[
    "capo_ec2.types.add_ipam_organizational_unit_exclusion.AddIpamOrganizationalUnitExclusion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddIpamOrganizationalUnitExclusionSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.add_ipam_organizational_unit_exclusion

        capo_ec2.types.add_ipam_organizational_unit_exclusion.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AddIpamOrganizationalUnitExclusionSet:
    import capo_ec2.types.add_ipam_organizational_unit_exclusion

    out: AddIpamOrganizationalUnitExclusionSet = []
    for child in el.findall("member"):
        out.append(
            capo_ec2.types.add_ipam_organizational_unit_exclusion.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> AddIpamOrganizationalUnitExclusionSet:
    import capo_ec2.types.add_ipam_organizational_unit_exclusion

    out: AddIpamOrganizationalUnitExclusionSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.add_ipam_organizational_unit_exclusion.deserialize_ec2_query(
                child
            )
        )
    return out
