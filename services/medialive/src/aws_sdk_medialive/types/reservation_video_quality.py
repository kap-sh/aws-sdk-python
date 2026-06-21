"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationVideoQuality``."""

from typing import Literal, TypeAlias, cast

"""Video quality, e.g. 'STANDARD' (Outputs only)"""
ReservationVideoQuality: TypeAlias = Literal[
    "STANDARD",
    "ENHANCED",
    "PREMIUM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationVideoQuality) -> str:
    return value


def deserialize_json(data: str) -> ReservationVideoQuality:
    return cast(ReservationVideoQuality, data)
