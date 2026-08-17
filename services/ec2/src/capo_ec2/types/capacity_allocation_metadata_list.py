"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocationMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_allocation_metadata_entry

CapacityAllocationMetadataList: TypeAlias = list[
    "capo_ec2.types.capacity_allocation_metadata_entry.CapacityAllocationMetadataEntry"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityAllocationMetadataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_allocation_metadata_entry

        capo_ec2.types.capacity_allocation_metadata_entry.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityAllocationMetadataList:
    import capo_ec2.types.capacity_allocation_metadata_entry

    out: CapacityAllocationMetadataList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_allocation_metadata_entry.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityAllocationMetadataList:
    import capo_ec2.types.capacity_allocation_metadata_entry

    out: CapacityAllocationMetadataList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_allocation_metadata_entry.deserialize_ec2_query(
                child
            )
        )
    return out
