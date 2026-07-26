"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

CapacityReservationPreference: TypeAlias = Literal[
    "capacity-reservations-only",
    "capacity-reservations-first",
    "none",
    "default",
]


# --- awsQuery ser/de ---
def to_query_text(value: CapacityReservationPreference) -> str:
    return value


def from_query_text(text: str) -> CapacityReservationPreference:
    return cast(CapacityReservationPreference, text)


def serialize_query(
    value: CapacityReservationPreference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CapacityReservationPreference:
    return from_query_text(el.text or "")
