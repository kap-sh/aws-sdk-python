"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationCodec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "MPEG2",
        "AVC",
        "HEVC",
        "AUDIO",
        "LINK",
        "AV1",
    )
)


def serialize_json(value: ReservationCodec) -> str:
    return value


def deserialize_json(data: str) -> ReservationCodec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReservationCodec value: {data!r}")
    return cast(ReservationCodec, data)
