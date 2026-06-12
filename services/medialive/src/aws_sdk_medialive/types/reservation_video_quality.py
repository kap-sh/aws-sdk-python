"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationVideoQuality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Video quality, e.g. 'STANDARD' (Outputs only)"""
ReservationVideoQuality: TypeAlias = Literal[
    "STANDARD",
    "ENHANCED",
    "PREMIUM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "ENHANCED",
        "PREMIUM",
    )
)


def serialize_json(value: ReservationVideoQuality) -> str:
    return value


def deserialize_json(data: str) -> ReservationVideoQuality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationVideoQuality value: {data!r}")
    return cast(ReservationVideoQuality, data)
