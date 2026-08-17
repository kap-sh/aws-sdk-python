"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetCancellationStateSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_fleet_cancellation_state

CapacityReservationFleetCancellationStateSet: TypeAlias = list[
    "capo_ec2.types.capacity_reservation_fleet_cancellation_state.CapacityReservationFleetCancellationState"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationFleetCancellationStateSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_reservation_fleet_cancellation_state

        capo_ec2.types.capacity_reservation_fleet_cancellation_state.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationFleetCancellationStateSet:
    import capo_ec2.types.capacity_reservation_fleet_cancellation_state

    out: CapacityReservationFleetCancellationStateSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_reservation_fleet_cancellation_state.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityReservationFleetCancellationStateSet:
    import capo_ec2.types.capacity_reservation_fleet_cancellation_state

    out: CapacityReservationFleetCancellationStateSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_reservation_fleet_cancellation_state.deserialize_ec2_query(
                child
            )
        )
    return out
