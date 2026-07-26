"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetCancellationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_fleet_id
    import capo_ec2.types.capacity_reservation_fleet_state


class CapacityReservationFleetCancellationState(TypedDict, closed=True):
    current_fleet_state: NotRequired[
        "capo_ec2.types.capacity_reservation_fleet_state.CapacityReservationFleetState"
    ]
    """<p>The current state of the Capacity Reservation Fleet.</p>"""
    previous_fleet_state: NotRequired[
        "capo_ec2.types.capacity_reservation_fleet_state.CapacityReservationFleetState"
    ]
    """<p>The previous state of the Capacity Reservation Fleet.</p>"""
    capacity_reservation_fleet_id: NotRequired[
        "capo_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet that was successfully cancelled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationFleetCancellationState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "current_fleet_state" in value:
        import capo_ec2.types.capacity_reservation_fleet_state

        capo_ec2.types.capacity_reservation_fleet_state.serialize_ec2_query(
            value["current_fleet_state"], pairs, f"{prefix}.CurrentFleetState"
        )
    if "previous_fleet_state" in value:
        import capo_ec2.types.capacity_reservation_fleet_state

        capo_ec2.types.capacity_reservation_fleet_state.serialize_ec2_query(
            value["previous_fleet_state"], pairs, f"{prefix}.PreviousFleetState"
        )
    if "capacity_reservation_fleet_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityReservationFleetId",
                str(value["capacity_reservation_fleet_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationFleetCancellationState:
    out: CapacityReservationFleetCancellationState = {}  # type: ignore[typeddict-item]
    child_current_fleet_state = el.find("CurrentFleetState")
    if child_current_fleet_state is not None:
        import capo_ec2.types.capacity_reservation_fleet_state

        out["current_fleet_state"] = (
            capo_ec2.types.capacity_reservation_fleet_state.deserialize_ec2_query(
                child_current_fleet_state
            )
        )
    child_previous_fleet_state = el.find("PreviousFleetState")
    if child_previous_fleet_state is not None:
        import capo_ec2.types.capacity_reservation_fleet_state

        out["previous_fleet_state"] = (
            capo_ec2.types.capacity_reservation_fleet_state.deserialize_ec2_query(
                child_previous_fleet_state
            )
        )
    child_capacity_reservation_fleet_id = el.find("CapacityReservationFleetId")
    if child_capacity_reservation_fleet_id is not None:
        out["capacity_reservation_fleet_id"] = str(
            child_capacity_reservation_fleet_id.text or ""
        )
    return out
