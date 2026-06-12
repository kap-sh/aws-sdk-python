"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationSpecialFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Special features, 'ADVANCED_AUDIO' 'AUDIO_NORMALIZATION' 'MGHD' or 'MGUHD'"""
ReservationSpecialFeature: TypeAlias = Literal[
    "ADVANCED_AUDIO",
    "AUDIO_NORMALIZATION",
    "MGHD",
    "MGUHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADVANCED_AUDIO",
        "AUDIO_NORMALIZATION",
        "MGHD",
        "MGUHD",
    )
)


def serialize_json(value: ReservationSpecialFeature) -> str:
    return value


def deserialize_json(data: str) -> ReservationSpecialFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationSpecialFeature value: {data!r}")
    return cast(ReservationSpecialFeature, data)
