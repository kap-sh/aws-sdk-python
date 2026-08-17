"""Generated from Smithy shape ``com.amazonaws.ec2#FailedCapacityReservationFleetCancellationResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result

FailedCapacityReservationFleetCancellationResultSet: TypeAlias = list[
    "capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result.FailedCapacityReservationFleetCancellationResult"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FailedCapacityReservationFleetCancellationResultSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result

        capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> FailedCapacityReservationFleetCancellationResultSet:
    import capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result

    out: FailedCapacityReservationFleetCancellationResultSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FailedCapacityReservationFleetCancellationResultSet:
    import capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result

    out: FailedCapacityReservationFleetCancellationResultSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.failed_capacity_reservation_fleet_cancellation_result.deserialize_ec2_query(
                child
            )
        )
    return out
