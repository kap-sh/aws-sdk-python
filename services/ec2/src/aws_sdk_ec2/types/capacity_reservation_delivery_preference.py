"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationDeliveryPreference``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

CapacityReservationDeliveryPreference: TypeAlias = Literal[
    "fixed",
    "incremental",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "fixed",
        "incremental",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "fixed",
        "incremental",
    )
)


def to_ec2_query_text(value: CapacityReservationDeliveryPreference) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationDeliveryPreference:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityReservationDeliveryPreference value: {text!r}"
        )
    return cast(CapacityReservationDeliveryPreference, text)


def serialize_ec2_query(
    value: CapacityReservationDeliveryPreference,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationDeliveryPreference:
    return from_ec2_query_text(el.text or "")
