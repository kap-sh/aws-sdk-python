"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationSpecialFeature``."""

from typing import Literal, TypeAlias, cast

"""Special features, 'ADVANCED_AUDIO' 'AUDIO_NORMALIZATION' 'MGHD' or 'MGUHD'"""
ReservationSpecialFeature: TypeAlias = Literal[
    "ADVANCED_AUDIO",
    "AUDIO_NORMALIZATION",
    "MGHD",
    "MGUHD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationSpecialFeature) -> str:
    return value


def deserialize_json(data: str) -> ReservationSpecialFeature:
    return cast(ReservationSpecialFeature, data)
