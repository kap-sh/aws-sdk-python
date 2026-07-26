"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAllocationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool_allocation

IpamPoolAllocationSet: TypeAlias = list[
    "capo_ec2.types.ipam_pool_allocation.IpamPoolAllocation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPoolAllocationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_pool_allocation

        capo_ec2.types.ipam_pool_allocation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> IpamPoolAllocationSet:
    import capo_ec2.types.ipam_pool_allocation

    out: IpamPoolAllocationSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_pool_allocation.deserialize_ec2_query(child))
    return out
