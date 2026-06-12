"""Generated from Smithy shape ``com.amazonaws.medialive#HlsDefault``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Default"""
HlsDefault: TypeAlias = Literal[
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


def serialize_json(value: HlsDefault) -> str:
    return value


def deserialize_json(data: str) -> HlsDefault:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsDefault value: {data!r}")
    return cast(HlsDefault, data)
