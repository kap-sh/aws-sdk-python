"""Generated from Smithy shape ``com.amazonaws.ec2#IpamInternetRegistryAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_internet_registry_association

IpamInternetRegistryAssociationSet: TypeAlias = list[
    "capo_ec2.types.ipam_internet_registry_association.IpamInternetRegistryAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamInternetRegistryAssociationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_internet_registry_association

        capo_ec2.types.ipam_internet_registry_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamInternetRegistryAssociationSet:
    import capo_ec2.types.ipam_internet_registry_association

    out: IpamInternetRegistryAssociationSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_internet_registry_association.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamInternetRegistryAssociationSet:
    import capo_ec2.types.ipam_internet_registry_association

    out: IpamInternetRegistryAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_internet_registry_association.deserialize_ec2_query(
                child
            )
        )
    return out
