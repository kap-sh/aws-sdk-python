"""Generated from Smithy shape ``com.amazonaws.medialive#HlsAutoSelect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Auto Select"""
HlsAutoSelect: TypeAlias = Literal[
    "NO",
    "OMIT",
    "YES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO",
        "OMIT",
        "YES",
    )
)


def serialize_json(value: HlsAutoSelect) -> str:
    return value


def deserialize_json(data: str) -> HlsAutoSelect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsAutoSelect value: {data!r}")
    return cast(HlsAutoSelect, data)
