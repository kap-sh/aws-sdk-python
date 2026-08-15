"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationCancellationQuoteState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityReservationCancellationQuoteState: TypeAlias = Literal[
    "pending",
    "active",
    "expired",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityReservationCancellationQuoteState) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationCancellationQuoteState:
    return cast(CapacityReservationCancellationQuoteState, text)


def serialize_ec2_query(
    value: CapacityReservationCancellationQuoteState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationCancellationQuoteState:
    return from_ec2_query_text(el.text or "")
