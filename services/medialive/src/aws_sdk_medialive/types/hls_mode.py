"""Generated from Smithy shape ``com.amazonaws.medialive#HlsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Mode"""
HlsMode: TypeAlias = Literal[
    "LIVE",
    "VOD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIVE",
        "VOD",
    )
)


def serialize_json(value: HlsMode) -> str:
    return value


def deserialize_json(data: str) -> HlsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsMode value: {data!r}")
    return cast(HlsMode, data)
