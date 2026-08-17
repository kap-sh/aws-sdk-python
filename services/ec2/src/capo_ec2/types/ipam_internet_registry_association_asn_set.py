"""Generated from Smithy shape ``com.amazonaws.ec2#IpamInternetRegistryAssociationAsnSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_internet_registry_association_asn

IpamInternetRegistryAssociationAsnSet: TypeAlias = list[
    "capo_ec2.types.ipam_internet_registry_association_asn.IpamInternetRegistryAssociationAsn"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamInternetRegistryAssociationAsnSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_internet_registry_association_asn

        capo_ec2.types.ipam_internet_registry_association_asn.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamInternetRegistryAssociationAsnSet:
    import capo_ec2.types.ipam_internet_registry_association_asn

    out: IpamInternetRegistryAssociationAsnSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_internet_registry_association_asn.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamInternetRegistryAssociationAsnSet:
    import capo_ec2.types.ipam_internet_registry_association_asn

    out: IpamInternetRegistryAssociationAsnSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_internet_registry_association_asn.deserialize_ec2_query(
                child
            )
        )
    return out
