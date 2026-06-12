"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2SubGopLength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mpeg2 Sub Gop Length"""
Mpeg2SubGopLength: TypeAlias = Literal[
    "DYNAMIC",
    "FIXED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DYNAMIC",
        "FIXED",
    )
)


def serialize_json(value: Mpeg2SubGopLength) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2SubGopLength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2SubGopLength value: {data!r}")
    return cast(Mpeg2SubGopLength, data)
