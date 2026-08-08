"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateInterruptibleCapacityReservationAllocationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_id
    import capo_ec2.types.integer
    import capo_ec2.types.interruptible_capacity_reservation_allocation_status
    import capo_ec2.types.interruption_type


class UpdateInterruptibleCapacityReservationAllocationResult(TypedDict, closed=True):
    interruptible_capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the interruptible Capacity Reservation that was modified. </p>"""
    source_capacity_reservation_id: NotRequired[
        "capo_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation to which capacity was reclaimed or from which capacity was allocated. </p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> The current number of instances allocated to the interruptible reservation. </p>"""
    target_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> The requested number of instances for the interruptible Capacity Reservation. </p>"""
    status: NotRequired[
        "capo_ec2.types.interruptible_capacity_reservation_allocation_status.InterruptibleCapacityReservationAllocationStatus"
    ]
    """<p> The current status of the allocation (updating during reclamation, active when complete). </p>"""
    interruption_type: NotRequired["capo_ec2.types.interruption_type.InterruptionType"]
    """<p> The interruption type for the interruptible reservation. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateInterruptibleCapacityReservationAllocationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "interruptible_capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}InterruptibleCapacityReservationId",
                str(value["interruptible_capacity_reservation_id"]),
            )
        )
    if "source_capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}SourceCapacityReservationId",
                str(value["source_capacity_reservation_id"]),
            )
        )
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "target_instance_count" in value:
        pairs.append(
            (f"{key_prefix}TargetInstanceCount", str(value["target_instance_count"]))
        )
    if "status" in value:
        import capo_ec2.types.interruptible_capacity_reservation_allocation_status

        capo_ec2.types.interruptible_capacity_reservation_allocation_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "interruption_type" in value:
        import capo_ec2.types.interruption_type

        capo_ec2.types.interruption_type.serialize_ec2_query(
            value["interruption_type"], pairs, f"{key_prefix}InterruptionType"
        )


def deserialize_ec2_query(
    el: Element,
) -> UpdateInterruptibleCapacityReservationAllocationResult:
    out: UpdateInterruptibleCapacityReservationAllocationResult = {}  # type: ignore[typeddict-item]
    child_interruptible_capacity_reservation_id = el.find(
        "interruptibleCapacityReservationId"
    )
    if child_interruptible_capacity_reservation_id is not None:
        out["interruptible_capacity_reservation_id"] = str(
            child_interruptible_capacity_reservation_id.text or ""
        )
    child_source_capacity_reservation_id = el.find("sourceCapacityReservationId")
    if child_source_capacity_reservation_id is not None:
        out["source_capacity_reservation_id"] = str(
            child_source_capacity_reservation_id.text or ""
        )
    child_instance_count = el.find("instanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_target_instance_count = el.find("targetInstanceCount")
    if child_target_instance_count is not None:
        out["target_instance_count"] = int(child_target_instance_count.text or "")
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.interruptible_capacity_reservation_allocation_status

        out["status"] = (
            capo_ec2.types.interruptible_capacity_reservation_allocation_status.deserialize_ec2_query(
                child_status
            )
        )
    child_interruption_type = el.find("interruptionType")
    if child_interruption_type is not None:
        import capo_ec2.types.interruption_type

        out["interruption_type"] = (
            capo_ec2.types.interruption_type.deserialize_ec2_query(
                child_interruption_type
            )
        )
    return out
