"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationAutomaticRenewal``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Automatic Renewal Status for Reservation"""
ReservationAutomaticRenewal: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "UNAVAILABLE",
    )
)


def serialize_json(value: ReservationAutomaticRenewal) -> str:
    return value


def deserialize_json(data: str) -> ReservationAutomaticRenewal:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReservationAutomaticRenewal value: {data!r}"
        )
    return cast(ReservationAutomaticRenewal, data)
