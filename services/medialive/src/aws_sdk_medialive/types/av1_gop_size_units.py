"""Generated from Smithy shape ``com.amazonaws.medialive#Av1GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Gop Size Units"""
Av1GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FRAMES",
        "SECONDS",
    )
)


def serialize_json(value: Av1GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> Av1GopSizeUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1GopSizeUnits value: {data!r}")
    return cast(Av1GopSizeUnits, data)
