"""Generated from Smithy shape ``com.amazonaws.ec2#FailedCapacityReservationFleetCancellationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error
    import aws_sdk_ec2.types.capacity_reservation_fleet_id


class FailedCapacityReservationFleetCancellationResult(TypedDict, closed=True):
    capacity_reservation_fleet_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet that could not be cancelled.</p>"""
    cancel_capacity_reservation_fleet_error: NotRequired[
        "aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error.CancelCapacityReservationFleetError"
    ]
    """<p>Information about the Capacity Reservation Fleet cancellation error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FailedCapacityReservationFleetCancellationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_reservation_fleet_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityReservationFleetId",
                str(value["capacity_reservation_fleet_id"]),
            )
        )
    if "cancel_capacity_reservation_fleet_error" in value:
        import aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error

        aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error.serialize_ec2_query(
            value["cancel_capacity_reservation_fleet_error"],
            pairs,
            f"{prefix}.CancelCapacityReservationFleetError",
        )


def deserialize_ec2_query(
    el: Element,
) -> FailedCapacityReservationFleetCancellationResult:
    out: FailedCapacityReservationFleetCancellationResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_fleet_id = el.find("CapacityReservationFleetId")
    if child_capacity_reservation_fleet_id is not None:
        out["capacity_reservation_fleet_id"] = str(
            child_capacity_reservation_fleet_id.text or ""
        )
    child_cancel_capacity_reservation_fleet_error = el.find(
        "CancelCapacityReservationFleetError"
    )
    if child_cancel_capacity_reservation_fleet_error is not None:
        import aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error

        out["cancel_capacity_reservation_fleet_error"] = (
            aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error.deserialize_ec2_query(
                child_cancel_capacity_reservation_fleet_error
            )
        )
    return out
