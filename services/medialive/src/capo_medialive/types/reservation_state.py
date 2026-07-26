"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationState``."""

from typing import Literal, TypeAlias, cast

"""Current reservation state"""
ReservationState: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "CANCELED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationState) -> str:
    return value


def deserialize_json(data: str) -> ReservationState:
    return cast(ReservationState, data)
