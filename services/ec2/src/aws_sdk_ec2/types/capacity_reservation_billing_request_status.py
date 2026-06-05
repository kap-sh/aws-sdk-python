"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationBillingRequestStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

CapacityReservationBillingRequestStatus: TypeAlias = Literal[
    "pending",
    "accepted",
    "rejected",
    "cancelled",
    "revoked",
    "expired",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "accepted",
        "rejected",
        "cancelled",
        "revoked",
        "expired",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "accepted",
        "rejected",
        "cancelled",
        "revoked",
        "expired",
    )
)


def to_ec2_query_text(value: CapacityReservationBillingRequestStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationBillingRequestStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityReservationBillingRequestStatus value: {text!r}"
        )
    return cast(CapacityReservationBillingRequestStatus, text)


def serialize_ec2_query(
    value: CapacityReservationBillingRequestStatus,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationBillingRequestStatus:
    return from_ec2_query_text(el.text or "")
