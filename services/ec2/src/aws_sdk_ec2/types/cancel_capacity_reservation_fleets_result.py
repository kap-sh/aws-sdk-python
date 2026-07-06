"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationFleetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set
    import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set


class CancelCapacityReservationFleetsResult(TypedDict, closed=True):
    successful_fleet_cancellations: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set.CapacityReservationFleetCancellationStateSet"
    ]
    """<p>Information about the Capacity Reservation Fleets that were successfully cancelled.</p>"""
    failed_fleet_cancellations: NotRequired[
        "aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set.FailedCapacityReservationFleetCancellationResultSet"
    ]
    """<p>Information about the Capacity Reservation Fleets that could not be cancelled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelCapacityReservationFleetsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "successful_fleet_cancellations" in value:
        import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set

        aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set.serialize_ec2_query(
            value["successful_fleet_cancellations"],
            pairs,
            f"{prefix}.SuccessfulFleetCancellationSet",
        )
    if "failed_fleet_cancellations" in value:
        import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set

        aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set.serialize_ec2_query(
            value["failed_fleet_cancellations"],
            pairs,
            f"{prefix}.FailedFleetCancellationSet",
        )


def deserialize_ec2_query(el: Element) -> CancelCapacityReservationFleetsResult:
    out: CancelCapacityReservationFleetsResult = {}  # type: ignore[typeddict-item]
    if el.find("SuccessfulFleetCancellationSet") is not None:
        import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set

        out["successful_fleet_cancellations"] = (
            aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set.deserialize_ec2_query(
                el, "SuccessfulFleetCancellationSet"
            )
        )
    if el.find("FailedFleetCancellationSet") is not None:
        import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set

        out["failed_fleet_cancellations"] = (
            aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set.deserialize_ec2_query(
                el, "FailedFleetCancellationSet"
            )
        )
    return out
