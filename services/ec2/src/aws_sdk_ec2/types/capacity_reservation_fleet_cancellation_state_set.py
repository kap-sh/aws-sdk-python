"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetCancellationStateSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state

CapacityReservationFleetCancellationStateSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state.CapacityReservationFleetCancellationState"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationFleetCancellationStateSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state

        aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> CapacityReservationFleetCancellationStateSet:
    import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state

    out: CapacityReservationFleetCancellationStateSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state.deserialize_ec2_query(
                child
            )
        )
    return out
