"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscoveryAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_resource_discovery_association

IpamResourceDiscoveryAssociationSet: TypeAlias = list[
    "capo_ec2.types.ipam_resource_discovery_association.IpamResourceDiscoveryAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceDiscoveryAssociationSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_resource_discovery_association

        capo_ec2.types.ipam_resource_discovery_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamResourceDiscoveryAssociationSet:
    import capo_ec2.types.ipam_resource_discovery_association

    out: IpamResourceDiscoveryAssociationSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_resource_discovery_association.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamResourceDiscoveryAssociationSet:
    import capo_ec2.types.ipam_resource_discovery_association

    out: IpamResourceDiscoveryAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_resource_discovery_association.deserialize_ec2_query(
                child
            )
        )
    return out
