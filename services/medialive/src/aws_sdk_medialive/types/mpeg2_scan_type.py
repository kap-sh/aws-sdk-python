"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2ScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mpeg2 Scan Type"""
Mpeg2ScanType: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERLACED",
        "PROGRESSIVE",
    )
)


def serialize_json(value: Mpeg2ScanType) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2ScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2ScanType value: {data!r}")
    return cast(Mpeg2ScanType, data)
