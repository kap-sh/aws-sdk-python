"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateInterruptibleCapacityReservationAllocationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer


class UpdateInterruptibleCapacityReservationAllocationRequest(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation containing the interruptible allocation to modify. </p>"""
    target_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The new number of instances to allocate. Enter a higher number to add more capacity to share, or a lower number to reclaim capacity to your source Capacity Reservation. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateInterruptibleCapacityReservationAllocationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "target_instance_count" in value:
        pairs.append(
            (f"{prefix}.TargetInstanceCount", str(value["target_instance_count"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> UpdateInterruptibleCapacityReservationAllocationRequest:
    out: UpdateInterruptibleCapacityReservationAllocationRequest = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_target_instance_count = el.find("TargetInstanceCount")
    if child_target_instance_count is not None:
        out["target_instance_count"] = int(child_target_instance_count.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
