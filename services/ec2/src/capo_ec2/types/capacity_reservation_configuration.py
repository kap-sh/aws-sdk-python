"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class CapacityReservationConfiguration(TypedDict, closed=True):
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Reservation.</p>"""
    reservation_state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of the Capacity Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "reservation_state" in value:
        pairs.append((f"{key_prefix}ReservationState", str(value["reservation_state"])))


def deserialize_ec2_query(el: Element) -> CapacityReservationConfiguration:
    out: CapacityReservationConfiguration = {}  # type: ignore[typeddict-item]
    child_instance_count = el.find("instanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_reservation_state = el.find("reservationState")
    if child_reservation_state is not None:
        out["reservation_state"] = str(child_reservation_state.text or "")
    return out
