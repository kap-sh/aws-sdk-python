"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscoverySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_resource_discovery

IpamResourceDiscoverySet: TypeAlias = list[
    "capo_ec2.types.ipam_resource_discovery.IpamResourceDiscovery"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceDiscoverySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_resource_discovery

        capo_ec2.types.ipam_resource_discovery.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamResourceDiscoverySet:
    import capo_ec2.types.ipam_resource_discovery

    out: IpamResourceDiscoverySet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_resource_discovery.deserialize_ec2_query(child))
    return out
