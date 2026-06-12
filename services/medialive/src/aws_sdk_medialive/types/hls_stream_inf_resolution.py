"""Generated from Smithy shape ``com.amazonaws.medialive#HlsStreamInfResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Stream Inf Resolution"""
HlsStreamInfResolution: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUDE",
        "INCLUDE",
    )
)


def serialize_json(value: HlsStreamInfResolution) -> str:
    return value


def deserialize_json(data: str) -> HlsStreamInfResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsStreamInfResolution value: {data!r}")
    return cast(HlsStreamInfResolution, data)
