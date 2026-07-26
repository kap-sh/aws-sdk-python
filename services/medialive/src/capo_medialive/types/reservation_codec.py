"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationCodec``."""

from typing import Literal, TypeAlias, cast

"""Codec, 'MPEG2', 'AVC', 'HEVC', 'AUDIO', 'LINK', or 'AV1'"""
ReservationCodec: TypeAlias = Literal[
    "MPEG2",
    "AVC",
    "HEVC",
    "AUDIO",
    "LINK",
    "AV1",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationCodec) -> str:
    return value


def deserialize_json(data: str) -> ReservationCodec:
    return cast(ReservationCodec, data)
