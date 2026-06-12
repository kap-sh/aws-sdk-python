"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ReservationPlanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED."""
ReservationPlanStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "EXPIRED",
    )
)


def serialize_json(value: ReservationPlanStatus) -> str:
    return value


def deserialize_json(data: str) -> ReservationPlanStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationPlanStatus value: {data!r}")
    return cast(ReservationPlanStatus, data)
