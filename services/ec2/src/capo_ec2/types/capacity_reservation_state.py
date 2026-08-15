"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityReservationState: TypeAlias = Literal[
    "active",
    "expired",
    "cancelled",
    "pending",
    "failed",
    "scheduled",
    "payment-pending",
    "payment-failed",
    "assessing",
    "delayed",
    "unsupported",
    "cancelling",
    "unavailable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityReservationState) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationState:
    return cast(CapacityReservationState, text)


def serialize_ec2_query(
    value: CapacityReservationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationState:
    return from_ec2_query_text(el.text or "")
