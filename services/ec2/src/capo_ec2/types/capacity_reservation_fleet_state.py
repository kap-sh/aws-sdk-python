"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityReservationFleetState: TypeAlias = Literal[
    "submitted",
    "modifying",
    "active",
    "partially_fulfilled",
    "expiring",
    "expired",
    "cancelling",
    "cancelled",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityReservationFleetState) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationFleetState:
    return cast(CapacityReservationFleetState, text)


def serialize_ec2_query(
    value: CapacityReservationFleetState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationFleetState:
    return from_ec2_query_text(el.text or "")
