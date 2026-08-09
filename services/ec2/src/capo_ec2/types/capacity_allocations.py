"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_allocation

CapacityAllocations: TypeAlias = list[
    "capo_ec2.types.capacity_allocation.CapacityAllocation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityAllocations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_allocation

        capo_ec2.types.capacity_allocation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityAllocations:
    import capo_ec2.types.capacity_allocation

    out: CapacityAllocations = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.capacity_allocation.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> CapacityAllocations:
    import capo_ec2.types.capacity_allocation

    out: CapacityAllocations = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.capacity_allocation.deserialize_ec2_query(child))
    return out
