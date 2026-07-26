"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ReservationState``."""

from typing import Literal, TypeAlias, cast

ReservationState: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "PROCESSING",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationState) -> str:
    return value


def deserialize_json(data: str) -> ReservationState:
    return cast(ReservationState, data)
