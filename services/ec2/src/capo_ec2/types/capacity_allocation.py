"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allocation_type
    import capo_ec2.types.capacity_allocation_metadata_list
    import capo_ec2.types.integer


class CapacityAllocation(TypedDict, closed=True):
    allocation_type: NotRequired["capo_ec2.types.allocation_type.AllocationType"]
    """<p>The usage type. <code>used</code> indicates that the instance capacity is in use by instances that are running in the Capacity Reservation.</p>"""
    count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The amount of instance capacity associated with the usage. For example a value of <code>4</code> indicates that instance capacity for 4 instances is currently in use.</p>"""
    allocation_metadata: NotRequired[
        "capo_ec2.types.capacity_allocation_metadata_list.CapacityAllocationMetadataList"
    ]
    """<p>Additional metadata associated with the capacity allocation. Each entry contains a key-value pair providing context about the allocation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityAllocation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "allocation_type" in value:
        import capo_ec2.types.allocation_type

        capo_ec2.types.allocation_type.serialize_ec2_query(
            value["allocation_type"], pairs, f"{prefix}.AllocationType"
        )
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))
    if "allocation_metadata" in value:
        import capo_ec2.types.capacity_allocation_metadata_list

        capo_ec2.types.capacity_allocation_metadata_list.serialize_ec2_query(
            value["allocation_metadata"], pairs, f"{prefix}.AllocationMetadataList"
        )


def deserialize_ec2_query(el: Element) -> CapacityAllocation:
    out: CapacityAllocation = {}  # type: ignore[typeddict-item]
    child_allocation_type = el.find("AllocationType")
    if child_allocation_type is not None:
        import capo_ec2.types.allocation_type

        out["allocation_type"] = capo_ec2.types.allocation_type.deserialize_ec2_query(
            child_allocation_type
        )
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    if el.find("AllocationMetadataList") is not None:
        import capo_ec2.types.capacity_allocation_metadata_list

        out["allocation_metadata"] = (
            capo_ec2.types.capacity_allocation_metadata_list.deserialize_ec2_query(
                el, "AllocationMetadataList"
            )
        )
    return out
