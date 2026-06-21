"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ReservationPlanStatus``."""

from typing import Literal, TypeAlias, cast

"""Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED."""
ReservationPlanStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationPlanStatus) -> str:
    return value


def deserialize_json(data: str) -> ReservationPlanStatus:
    return cast(ReservationPlanStatus, data)
