"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

CapacityReservationPreference: TypeAlias = Literal[
    "capacity-reservations-only",
    "capacity-reservations-first",
    "none",
    "default",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "capacity-reservations-only",
        "capacity-reservations-first",
        "none",
        "default",
    )
)


def to_query_text(value: CapacityReservationPreference) -> str:
    return value


def from_query_text(text: str) -> CapacityReservationPreference:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityReservationPreference value: {text!r}"
        )
    return cast(CapacityReservationPreference, text)


def serialize_query(
    value: CapacityReservationPreference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CapacityReservationPreference:
    return from_query_text(el.text or "")
