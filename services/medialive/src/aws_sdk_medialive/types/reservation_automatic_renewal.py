"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationAutomaticRenewal``."""

from typing import Literal, TypeAlias, cast

"""Automatic Renewal Status for Reservation"""
ReservationAutomaticRenewal: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationAutomaticRenewal) -> str:
    return value


def deserialize_json(data: str) -> ReservationAutomaticRenewal:
    return cast(ReservationAutomaticRenewal, data)
