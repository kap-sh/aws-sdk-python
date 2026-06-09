"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInterruptibleCapacityReservationAllocationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status
    import aws_sdk_ec2.types.interruption_type


class CreateInterruptibleCapacityReservationAllocationResult(TypedDict):
    source_capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation from which the interruptible Capacity Reservation was created. </p>"""
    target_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The number of instances allocated to the interruptible reservation. </p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status.InterruptibleCapacityReservationAllocationStatus"
    ]
    """<p> The current status of the allocation request (creating, active, updating). </p>"""
    interruption_type: NotRequired[
        "aws_sdk_ec2.types.interruption_type.InterruptionType"
    ]
    """<p> The type of interruption applied to the interruptible reservation. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInterruptibleCapacityReservationAllocationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "source_capacity_reservation_id" in value:
        pairs.append(
            (
                f"{prefix}.SourceCapacityReservationId",
                str(value["source_capacity_reservation_id"]),
            )
        )
    if "target_instance_count" in value:
        pairs.append(
            (f"{prefix}.TargetInstanceCount", str(value["target_instance_count"]))
        )
    if "status" in value:
        import aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status

        aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "interruption_type" in value:
        import aws_sdk_ec2.types.interruption_type

        aws_sdk_ec2.types.interruption_type.serialize_ec2_query(
            value["interruption_type"], pairs, f"{prefix}.InterruptionType"
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateInterruptibleCapacityReservationAllocationResult:
    out: CreateInterruptibleCapacityReservationAllocationResult = {}  # type: ignore[typeddict-item]
    child_source_capacity_reservation_id = el.find("SourceCapacityReservationId")
    if child_source_capacity_reservation_id is not None:
        out["source_capacity_reservation_id"] = str(
            child_source_capacity_reservation_id.text or ""
        )
    child_target_instance_count = el.find("TargetInstanceCount")
    if child_target_instance_count is not None:
        out["target_instance_count"] = int(child_target_instance_count.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status

        out["status"] = (
            aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status.deserialize_ec2_query(
                child_status
            )
        )
    child_interruption_type = el.find("InterruptionType")
    if child_interruption_type is not None:
        import aws_sdk_ec2.types.interruption_type

        out["interruption_type"] = (
            aws_sdk_ec2.types.interruption_type.deserialize_ec2_query(
                child_interruption_type
            )
        )
    return out
