"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Scte35 Type"""
Scte35Type: TypeAlias = Literal[
    "NONE",
    "SCTE_35_WITHOUT_SEGMENTATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SCTE_35_WITHOUT_SEGMENTATION",
    )
)


def serialize_json(value: Scte35Type) -> str:
    return value


def deserialize_json(data: str) -> Scte35Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scte35Type value: {data!r}")
    return cast(Scte35Type, data)
