"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2DisplayRatio``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mpeg2 Display Ratio"""
Mpeg2DisplayRatio: TypeAlias = Literal[
    "DISPLAYRATIO16X9",
    "DISPLAYRATIO4X3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISPLAYRATIO16X9",
        "DISPLAYRATIO4X3",
    )
)


def serialize_json(value: Mpeg2DisplayRatio) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2DisplayRatio:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2DisplayRatio value: {data!r}")
    return cast(Mpeg2DisplayRatio, data)
