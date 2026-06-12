"""Generated from Smithy shape ``com.amazonaws.medialive#Av1BitDepth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Av1 Bit Depth"""
Av1BitDepth: TypeAlias = Literal[
    "DEPTH_10",
    "DEPTH_8",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPTH_10",
        "DEPTH_8",
    )
)


def serialize_json(value: Av1BitDepth) -> str:
    return value


def deserialize_json(data: str) -> Av1BitDepth:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1BitDepth value: {data!r}")
    return cast(Av1BitDepth, data)
